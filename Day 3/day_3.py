import re


with open("day3_data.txt", "r") as corrupted_file:
    content = corrupted_file.read()
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    dos = re.compile(r"do\(\)")
    donts = re.compile(r"don't\(\)")
    
    hits = pattern.finditer(content)
    do_matches = dos.finditer(content)
    dont_matches = donts.finditer(content)


#### Solving by Using Regex ####

on = True 
total = 0

for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", content):
    if match == "do()":
        on = True
    elif match == "don't()":
        on = False 
    elif on:
        x, y = map(int, match[4:-1].split(","))
        total += x * y

print(total)



### Solving By Using a Hash-Table ####

# hash = {0: True,}

# for match in do_matches:
#     hash[match.span()[0]] = True

# for match in dont_matches:
#     hash[match.span()[0]] = False


# total = 0 
# enabled = True
# counter = 0 
# for hit in hits:
#     start = hit.span()[0]
#     while counter != start:
#         counter += 1
#         if counter in hash:
#             enabled = hash[counter]
    
#     if enabled:
#         temp = re.findall('\d+', hit.group())
#         total += int(temp[0]) * int(temp[1])

# print(total)