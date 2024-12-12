import re

hash_rules = {}
correct_updates = []
incorrect_updates = []
total = 0

with open("day_5_data.txt", "r") as file:
    content = file.read()
    pattern = re.compile(r"\d+\|\d+")


    rules = pattern.finditer(content)
    
    for rule in rules:
        x, y = map(int, rule.group().split("|"))
        if x not in hash_rules:
            hash_rules[x] = {y}
        else:
            hash_rules[x].add(y)

    all_content = content.split("\n")
    all_updates = []
    for c in all_content:
        if c == '' or c[2]== '|':
            pass
        else:
            all_updates.append(list(map(int, c.split(","))))
    
    temp_set = set()

    for update in all_updates:
        broke = False
        for n in update:
            temp_set.add(n)
            if n not in hash_rules:
                pass
            else:
                if temp_set.isdisjoint(hash_rules[n]) == False:
                    temp_set = set()
                    broke = True
                    incorrect_updates.append(update)
                    break

        if broke == False:
            correct_updates.append(update)
            total += update[(len(update) // 2)]
        temp_set = set()
print(total)