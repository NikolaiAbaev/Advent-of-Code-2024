disk = []
file_id = 0

for i, char in enumerate(#paste a string of input here):
    x = int(char)
    if i % 2 == 0:
        disk += [file_id] * x
        file_id += 1
    else:
        disk += [-1] * x

blanks = [i for i, x in enumerate(disk) if x == -1]

for i in blanks:
    while disk[-1] == -1: disk.pop()
    if len(disk) <= i: break
    disk[i] = disk.pop()

print(sum(i * x for i, x in enumerate(disk)))