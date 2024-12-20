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
    for v in range(len(value)):
        for j in range(v + 1, len(value)):
            r1, c1 = value[v]
            r2, c2 = value[j]
            dr, dc = r2 - r1, c2 - c1
            
            location_1 = (r1 - dr, c1 -dc)
            if -1 < location_1[0] < cols and -1 < location_1[1] < rows:
                unique_locations.add(tuple(location_1))
            
            location_2 = (r2 + dr, c2 + dc)
            if -1 < location_2[0] < cols and -1 < location_2[1] < cols:
                unique_locations.add(tuple(location_2))

