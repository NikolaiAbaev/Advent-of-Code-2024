import re

hash_rules = {}
correct_updates = []

with open("day_5_data.txt", "r") as file:
    content = file.read()
    pattern = re.compile(r"\d+\|\d+")


    rules = pattern.finditer(content)
    
    for rule in rules:
        x, y = map(int, rule.group().split("|"))
        if x not in hash_rules:
            hash_rules[x] = [y]
        else:
            hash_rules[x].append(y)

    all_content = content.split("\n")
    all_updates = []
    for c in all_content:
        if c == '' or c[2]== '|':
            pass
        else:
            all_updates.append(list(map(int, c.split(","))))

    temp_set = {}
    for update in all_updates:
        
        if temp_set in hash_rules[update]:
