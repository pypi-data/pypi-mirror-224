import asyncio
from aiohttp_xmlrpc.client import ServerProxy


client = ServerProxy("https://koji.fedoraproject.org/kojihub")

async def main():
    repo = await client.getRepo("f38-build")
    latest_tagged_builds = await client.listTagged("f38-build", dict(__starstar=True, event=repo["create_event"], inherit=True, latest=True, package="gtk3"))
    print(latest_tagged_builds[0]["nvr"])
    print(await client.getTaskInfo(101129116))
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
