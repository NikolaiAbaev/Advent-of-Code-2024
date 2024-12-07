#### Part I -- Finding the Distance

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

print(f'Distance is {distance}')

#### Part II -- FInding Similarity Score
hash_right = {}
similarity_score = 0

for i in right:
    if i not in hash_right:
        hash_right[i] = 1
    else:
        hash_right[i] += 1

for i in left: 
    if i not in hash_right:
        pass
    else:
        similarity_score += i * hash_right[i]

print(f'Similarity Score is {similarity_score}')