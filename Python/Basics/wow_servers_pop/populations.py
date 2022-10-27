# Search mode to find server and it's population by name.

population = open("D:\Projects\devop-learn\Python\servers_population.txt", 'r')

print("Reading file ...", end="")
lines = []
for line in population:
    lines.append(line.split())
print("[OK]")

print("Creating server-population dictionary ... ", end="")
servers_info = {}
for i, line in enumerate(lines):
    if i == 0:
        continue
    server_name = line[0]
    server_total_population = float(line[-1].replace(',', ''))
    servers_info.update({server_name: server_total_population})
print("[OK]")

print("Sorting dictionary ... ", end="")
servers_info = dict(sorted(
    servers_info.items(), key=lambda item: item[1]))
print("[OK]\n")


most_populated = list(servers_info)[-1]
print(
    f"Most populated server: {most_populated.upper()} with population of {servers_info[most_populated]}")

searching = True
server_names = [name.lower() for name in servers_info.keys()]

while searching:
    server_name = input("Search by server name: ").lower()
    if server_name in server_names:
        for name, population in servers_info.items():
            if server_name == name.lower():
                print(f"=====[{name.upper()}: {population}]=====")
                continue
    else:
        print(f"Could not find '{server_name}'.")
        server_name = ""
