import functools


content = open('day_5_data.txt', 'r')
rules = []

for line in content:
    if line.isspace(): break
    rules.append(list(map(int, line.split("|"))))

cache = {}
for x, y in rules:
    cache[(x, y)] = -1
    cache[(y, x)] = 1


def is_valid(updates):
    for i in range(len(updates)):
        for j in range(i + 1, len(updates)):
            if (updates[i], updates[j]) in cache and cache[(updates[i], updates[j])] == 1:
                return False
    return True


def compare_func(x, y):
    return cache.get((x, y), 0)


total = 0
for line in content:
    updates = list(map(int, line.split(",")))
    if is_valid(updates): continue
    updates.sort(key=functools.cmp_to_key(compare_func))
    total += updates[len(updates) // 2]