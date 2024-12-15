cols, rows = 50, 50

antenna_map = []

antenna_hash = {'F': [[0, 2], [4, 3], [7, 19], [9, 4]], 'L': [[0, 13], [1, 28], [3, 15], [10, 0]],}
unique_locations = set()


for i in range(cols):
    antenna_map.append([])
    for j in range(rows):
        antenna_map[i].append('.')


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


for key, value in antenna_hash.items():
    for v in value:
        antenna_map[v[0]][v[1]] = key

print(len(unique_locations))
print(unique_locations)
