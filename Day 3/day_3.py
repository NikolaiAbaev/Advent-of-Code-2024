import re


with open("day3_data.txt", "r") as corrupted_file:
    content = corrupted_file.read()
    pattern = r"mul\((\d+),(\d+)\)"
    hits = re.findall(pattern, content)

total = 0

for mul in hits:
    product = int(mul[0]) *  int(mul[1])
    total += product

