antenna_map = []
antenna_hash = {}
unique_locations = set()

with open("day_8_data.txt", "r") as file:
    content = file.read().splitlines()
    for line in content:
        antenna_map.append(list(line))


cols, rows = len(antenna_map[0]), len(antenna_map)


for column in range(cols):
    for item in range(rows):
        if antenna_map[column][item].isalnum():
            if antenna_map[column][item] not in antenna_hash:
                antenna_hash[antenna_map[column][item]] = [[column, item]]
            else:
                antenna_hash[antenna_map[column][item]].append([column, item])


for key, value in antenna_hash.items():
    for i in range(len(value)):
        for j in range(len(value)):
            if i == j: continue

            r1, c1 = value[i]
            r2, c2 = value[j]
            dr, dc = r2 - r1, c2 - c1
            r = r1
            c = c1 

            while -1 < r < rows and -1 < c < cols:
                unique_locations.add((r, c))
                r += dr
                c += dc 

print(len(unique_locations)) 
