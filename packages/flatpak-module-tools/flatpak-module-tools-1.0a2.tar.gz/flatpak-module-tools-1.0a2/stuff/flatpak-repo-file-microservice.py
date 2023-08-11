import re
from textwrap import dedent

from flask import Flask, make_response
import koji

app = Flask(__name__)


@app.route("/repos/f<int:version>/<runtime>.repo")
def repo(version, runtime):
    if not re.match('^[A-Za-z0-9.+_-]{1,100}$', runtime):
        response = make_response("Invalid runtime name", 400)
        response.mimetype = "text/plain"
        return response

    options = koji.read_config(profile_name='koji')
    session_opts = koji.grab_session_options(options)
    session = koji.ClientSession(options['server'], session_opts)

    # To find the latest built runtime, look up it up in the dest
    # We find the dest tag from the target, since it will change
    # from f38-flatpak-candidate to f38-flatpak-updates-candidate
    flatpak_target = f"f{version}-flatpak-candidate"
    
    flatpak_target_info = session.getBuildTarget(flatpak_target)
    if flatpak_target_info is None:
        response = make_response(f"Fedora version {version} not found", 404)
        response.mimetype = "text/plain"
        return response

    flatpak_dest_tag = flatpak_target_info["dest_tag_name"]

    # Now look up the latest build
    tagged_builds = session.listTagged(
        flatpak_dest_tag, package=runtime, latest=True, inherit=True,
    )
    if len(tagged_builds) == 0:
        response = make_response(f"Can't find build for '{runtime}' in {flatpak_dest_tag}", 404)
        response.mimetype = "text/plain"
        return response

    latest_build = tagged_builds[0]

    # Look up the RPMs in the container from koji. When building a container,
    # we want to prefer getting the normal (prefix=/usr) versions of these
    # packages. For everything else, we want the rebuilt (prefix=/app) versions.
    archives = session.listArchives(buildID=latest_build["build_id"])
    archive = next(a for a in archives if a["extra"]["image"]["arch"] == "x86_64")

    runtime_rpms = session.listRPMs(imageID=archive["id"])
    runtime_rpm_names = [rpm["name"] for rpm in runtime_rpms]

    disttag = f".fc{version}app"

    repos = dedent(f"""\
        [{runtime}-f{version}]
        baseurl=https://kojipkgs.fedoraproject.org/repos/f{version}-flatpak-runtime-build/latest/$basearch/
        includepkgs={",".join(sorted(runtime_rpm_names))}
        enabled=1
        priority=10
        skip_if_unavailable=False

        [f{version}-flatpak-app-build]
        baseurl=https://kojipkgs.fedoraproject.org/repos/f{version}-flatpak-app-build/latest/$basearch/
        enabled=1
        includepkgs=*{disttag}
        priority=20
        skip_if_unavailable=False
        """)

    response = make_response(repos)
    response.mimetype = "text/plain"
    return response
