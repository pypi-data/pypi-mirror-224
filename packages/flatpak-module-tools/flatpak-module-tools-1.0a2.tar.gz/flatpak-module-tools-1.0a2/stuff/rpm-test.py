import rpm

#rpm.addMacro('_dbpath','/var/lib/rpm')
rpm.addMacro('_dbpath','/var/lib/mock/flatpak-module-f38-x86_64/root/usr/lib/sysimage/rpm')
ts = rpm.TransactionSet()
ts.openDB()
rpm.delMacro('_dbpath')

all = set()
mi = ts.dbMatch()
for h in mi:
    if any(d.startswith("/app/") for d in h['dirnames']):
        all.add(f"{h['name']}-{h['version']}-{h['release']}.{h['arch']}-{h['sigmd5'].hex()}-{h['size']}")

for nvr in sorted(all):
    print(nvr)

