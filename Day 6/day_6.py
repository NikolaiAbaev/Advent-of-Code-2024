content = open('day_6_data.txt', 'r').read().splitlines()
lab_map = list(map(list, content))
cols, rows, = len(lab_map[0]), len(lab_map)

def move_guard(current_location, symbol):
    x = current_location[0]
    y = current_location[1]
    
    if symbol == '^':
        x -= 1
    elif symbol == 'v':
        x += 1
    elif symbol == '<':
        y -= 1
    elif symbol == '>':
        y += 1   
    list_location = [x, y]
    return list_location


def symbol_update(symbol):
    if symbol == '^':
        return '>'
    elif symbol == '>':
        return 'v'
    elif symbol == 'v':
        return '<'
    elif symbol == '<':
        return '^'
    

for i in range(rows):
    for j in range(cols):
        if lab_map[i][j] == '^':
            break
    else:
        continue
    break
guard_location = [i, j]

while True:    
    symbol = lab_map[guard_location[0]][guard_location[1]]
    updated_move = move_guard(guard_location, symbol)

    if updated_move[0] < 0 or updated_move[0] > rows - 1 or updated_move[1] < 0 or updated_move[1] > cols - 1:
        break

    next_cell = lab_map[updated_move[0]][updated_move[1]]

    if next_cell == '.':
        lab_map[guard_location[0]][guard_location[1]] = 'X'
        guard_location = updated_move
        lab_map[guard_location[0]][guard_location[1]] = symbol

    if next_cell == '#':
        lab_map[guard_location[0]][guard_location[1]] = 'X'
        symbol = symbol_update(symbol)
        lab_map[guard_location[0]][guard_location[1]] = symbol

    if next_cell == 'X':
        lab_map[guard_location[0]][guard_location[1]] = 'X'
        guard_location = updated_move
        lab_map[guard_location[0]][guard_location[1]] = symbol 

counter = 1
for i in lab_map:
    for j in i:
        if j == 'X':
            counter += 1

print(counter)