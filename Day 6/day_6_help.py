content = open('day_6_data.txt', 'r').read().splitlines()
lab_map = list(map(list, content))
cols, rows, = len(lab_map[0]), len(lab_map)


for r in range(rows):
    for c in range(cols):
        if lab_map[r][c] == '^':
            break
    else:
        continue
    break


def check_loop(grid, r, c):
    seen = set()
    
    dr = -1
    dc = 0  
    
    while True:
        seen.add((r, c, dr, dc))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols: 
            return False
        
        if grid[r + dr][c + dc] == '#':
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in seen: 
            return True

counter = 0 
for cr in range(rows):
    for cc in range(cols):
        if lab_map[cr][cc] != '.': continue
        else:
            lab_map[cr][cc] = '#'
            if check_loop(lab_map, r, c):
                counter += 1
            lab_map[cr][cc] = '.'

print(counter)