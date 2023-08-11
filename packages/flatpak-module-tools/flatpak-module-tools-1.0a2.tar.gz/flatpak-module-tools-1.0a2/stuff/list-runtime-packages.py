#!/usr/bin/python3

import click
import json
import networkx
import subprocess
from tempfile import NamedTemporaryFile
import koji
import sys

from flatpak_module_tools.utils import info


def _transitive_reduction(G):
    """ Returns transitive reduction of a directed graph
    The transitive reduction of G = (V,E) is a graph G- = (V,E-) such that
    for all v,w in V there is an edge (v,w) in E- if and only if (v,w) is
    in E and there is no path from v to w in G with length greater than 1.
    Parameters
    ----------
    G : NetworkX DiGraph
        A directed acyclic graph (DAG)
    Returns
    -------
    NetworkX DiGraph
        The transitive reduction of `G`
    Raises
    ------
    NetworkXError
        If `G` is not a directed acyclic graph (DAG) transitive reduction is
        not uniquely defined and a :exc:`NetworkXError` exception is raised.
    References
    ----------
    https://en.wikipedia.org/wiki/Transitive_reduction
    """
    if not networkx.algorithms.dag.is_directed_acyclic_graph(G):
        raise networkx.NetworkXError(
            "Transitive reduction only uniquely defined on directed acyclic graphs.")
    TR = networkx.DiGraph()
    TR.add_nodes_from(G.nodes())
    for u in G:
        u_edges = set(G[u])
        for v in G[u]:
            u_edges -= {y for x, y in networkx.dfs_edges(G, v)}
        TR.add_edges_from((u, v) for v in u_edges)
    return TR


def list_runtime_packages(session, name, fedora_release):
    runtime_package_id = session.getPackageID(name)
    all_builds = session.listBuilds(packageID=runtime_package_id, type="image")
    builds = [b for b in all_builds if b["version"] == f"f{fedora_release}"]
    latest_build = builds[-1]

    archives = session.listArchives(buildID=latest_build["build_id"])
    archive = next(a for a in archives if a["extra"]["image"]["arch"] == "x86_64")

    rpms = session.listRPMs(imageID=archive["id"])
    return [rpm["name"] for rpm in rpms]


_FLAGS_TO_REL = {
    koji.RPMSENSE_LESS: "<",
    koji.RPMSENSE_LESS | koji.RPMSENSE_EQUAL: "<=",
    koji.RPMSENSE_EQUAL: "=",
    koji.RPMSENSE_GREATER: ">",
    koji.RPMSENSE_GREATER | koji.RPMSENSE_EQUAL: ">=",
}

RPMSENSE_RPMLIB = (1 << 24)  # rpmlib(feature) dependency.


def flags_to_rel(flags):
    return _FLAGS_TO_REL[flags & (koji.RPMSENSE_LESS | koji.RPMSENSE_EQUAL | koji.RPMSENSE_GREATER)]


def get_build_requires(session, build_id):
    latest_src_rpm = session.listRPMs(build_id, arches=["src"])[0]
    result = []

    deps = session.getRPMDeps(latest_src_rpm["id"], depType=koji.DEP_REQUIRE)
    for dep in deps:
        if dep["flags"] & RPMSENSE_RPMLIB != 0:
            continue
        if dep["version"] != "":
            result.append(f"{dep['name']} {flags_to_rel(dep['flags'])} {dep['version']}")
        else:
            result.append(dep["name"])

    return result


def print_explanation(explanation, prefix, buildrequiring=None):
    if explanation is None:
        print(f"{prefix}<in input>")
    else:
        if len(explanation) % 2 == 0:
            provide = explanation[0]
            provided_by = explanation[1]
            print(f"{prefix}{buildrequiring} buildrequires {provide}, provided by {provided_by}")
            start = 1
        else:
            start = 0

        for i in range(start, len(explanation) - 2, 2):
            required_by = explanation[i]
            provide = explanation[i + 1]
            provided_by = explanation[i + 2]
            print(f"{prefix}{required_by} requires {provide}, provided by {provided_by}")


def build_order(build_after, build_after_details):
    if len(build_after) == 1:
        # No need to buildorder a single SRPM. There might be a cycle from
        # the SRPM to itself, but we assume that we don't care. (We could
        # try to ignore such cycles more generally - might get tricky.)
        return {list(build_after)[0]: 1}

    G = networkx.DiGraph()
    G.add_nodes_from(build_after)
    for package, after in build_after.items():
        for name in after:
            G.add_edge(package, name)

    cycles = list()
    cycles_iter = networkx.simple_cycles(G)
    for cycle in cycles_iter:
        cycles.append(cycle)
        if len(cycles) == 25:
            break

    cycles.sort(key=lambda x: len(x))
    for c in cycles[0:5]:
        print("Found cycle")
        for i, x in     erate(c):
            y = c[(i + 1) % len(c)]
            print(f"    {x} ⇒ {y}")
            print_explanation(
                build_after_details[x][y][0]["explanation"],
                prefix="        ",
                buildrequiring=x
            )
        print()

    if len(cycles) > 5:
        print("More than 5 cycles found, ignoring additional cycles")

    if len(cycles) > 0:
        sys.exit(0)

    G = _transitive_reduction(G)

    order_map = {}
    order = 1
    while len(order_map) < len(build_after):
        for name in build_after:
            if name in order_map:
                continue

            all_ordered = True
            for _, other in G.out_edges(name):
                if order_map.get(other, order) == order:
                    all_ordered = False
                    break
            if all_ordered:
                order_map[name] = order
        order += 1

    return order_map


def main():
    options = koji.read_config(profile_name='koji')
    session_opts = koji.grab_session_options(options)
    session = koji.ClientSession(options['server'], session_opts)

    info("Listing runtime package")
    runtime_packages = list_runtime_packages(session, "flatpak-runtime", "38")

    info(f"Finding dependencies of {sys.argv[1]} not in runtime")
    with NamedTemporaryFile(
        mode="w", prefix="flatpak-runtime-f38", suffix=".packages"
    ) as runtime_tempfile:
        for pkg in runtime_packages:
            print(pkg, file=runtime_tempfile)
        runtime_tempfile.flush()

        output = subprocess.check_output(
            ["flatpak-module-depchase",
             "--local-repo=local:x86_64/rpms",
             "resolve-packages",
             "--source",
             "--json",
             "--ignore-requires=mediawriter:polkit",
             "--ignore-requires=mediawriter:storaged",
             "--preinstalled",
             runtime_tempfile.name,
             sys.argv[1]]
        )

    build_after = {}
    build_after_details = {}

    data = json.loads(output)
    print("Needed for installation:")

    to_rebuild = []
    for source_rpm, binary_rpm_details in data.items():
        all_rebuilt = True
        for details in binary_rpm_details:
            release_arch = details["nvra"].rsplit("-", 2)[2]
            release = release_arch.rsplit(".", 1)[0]
            if details["repo"] == "local":
                repo = " (local)"
            else:
                repo = ""
            if not release.endswith("app"):
                all_rebuilt = False
                click.secho(f"    {details['nvra']}{repo}", bold=True)
            else:
                click.secho(f"    {details['nvra']}{repo}")
        if not all_rebuilt:
            to_rebuild.append(source_rpm)

    print("To rebuild:", ", ".join(to_rebuild))

    while True:
        choice = click.prompt("Proceed?", type=click.Choice(["y", "n", "?"]))
        if choice == "y":
            break
        if choice == "n":
            return

        for source_rpm, binary_rpm_details in data.items():
            print(source_rpm)
            for details in binary_rpm_details:
                print(f"    {details['name']}")
                if "explanation" in details:
                    print_explanation(details["explanation"], "        ")
                else:
                    print("        <in input>")

    info("Getting latest builds from koji")
    latest_builds = {}
    for source_rpm in data:
        latest_builds[source_rpm] = session.listTagged(
            "f38-updates-candidate", package=source_rpm, inherit=True, latest=True
        )[0]

    info("Getting build requirements from koji")
    build_requires_map = {}
    for source_rpm in to_rebuild:
        build_requires_map[source_rpm] = \
            get_build_requires(session, latest_builds[source_rpm]["id"])

    info("Expanding build requirements, to determine order")
    for source_rpm in to_rebuild:
        build_requires = build_requires_map[source_rpm]
        if not build_requires:
            build_after[source_rpm] = set()
            print(f"{source_rpm}: after: <nothing>")
            continue

        print(source_rpm, end="")

        with NamedTemporaryFile(
            mode="w", prefix="flatpak-runtime-f38", suffix=".packages"
        ) as runtime_tempfile:
            for pkg in runtime_packages:
                print(pkg, file=runtime_tempfile)
            runtime_tempfile.flush()

            # print(" ".join(f'"{x}"' for x in build_requires))
            output = subprocess.check_output(
                ["flatpak-module-depchase",
                 "--refresh=missing",
                 "resolve-requires",
                 "--source",
                 "--json",
                 "--preinstalled",
                 runtime_tempfile.name] + build_requires
            )

        resolved_build_requires = json.loads(output)
        after = {
            required_name for required_name in resolved_build_requires
            if required_name != source_rpm and required_name in to_rebuild
        }
        build_after[source_rpm] = after

        build_after_details[source_rpm] = {
            required_name: details for required_name, details in resolved_build_requires.items()
            if required_name != source_rpm and required_name in data
        }

        if after:
            print(": after: ", " ".join(sorted(after)))
            continue
        else:
            print(": after: <nothing>")

    print(build_after)

    info("Determining build batches")
    order_map = build_order(build_after, build_after_details)
    n_batches = max(order_map.values())
    batches = []
    for i in range(1, n_batches + 1):
        batch = sorted(n for n, v in order_map.items() if v == i)
        batches.append(batch)
        print(f"Batch {i}:", " ".join(batch))

    click.confirm("Proceed?")


if __name__ == "__main__":
    main()
