import re


with open("day3_data.txt", "r") as corrupted_file:
    content = corrupted_file.read()
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    dos = re.compile(r"do\(\)")
    donts = re.compile(r"don't\(\)")
    
    hits = pattern.finditer(content)
    do_matches = dos.finditer(content)
    dont_matches = donts.finditer(content)

hash = {0: True,}

for match in do_matches:
    hash[match.span()[0]] = True

for match in dont_matches:
    hash[match.span()[0]] = False


for hit in hits:
    temp = hit.group()
    print(temp)

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

