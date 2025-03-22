import json

with open('sample-data.json', "r") as file:
    data = json.load(file)

out = []
out.append("Interface Status")
out.append("=" * 90)
out.append(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
out.append("-" * 90)

for i in data["imdata"]:
    b = i["l1PhysIf"]["attributes"]
    out.append(f"{b["dn"]:<50} {b["pathSDescr"]:<20} {b["speed"]:<10} {b["mtu"]:<10}")

for i in out:
    print(i)