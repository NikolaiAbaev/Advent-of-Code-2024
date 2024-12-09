#Part I 
count = 0 
all_codes = []

def is_safe(list) -> int:
    diffs = [x - y for x, y in zip(list, list[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)

with open("data.txt", "r") as file: 
    for line in file:
        strip = line.rstrip().split()
        temp = []
        for i in strip:
            temp.append(int(i))

        if is_safe(temp):
            count += 1

print(count)