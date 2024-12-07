left = []
right = []

distance = 0 

with open("data.txt", "r") as file:
    for line in file:
        strip = line.rstrip().split()
        left.append(int(strip[0]))
        right.append(int(strip[1]))

left.sort()
right.sort()

for i in range(len(left)):
    x = left[i] - right[i]
    if x < 0:
        x *= -1 
    distance += x