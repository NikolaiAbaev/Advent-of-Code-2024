content = open("day_7_data.txt", "r").read().splitlines()
hash = {}
counter = 0


for line in content:
    update = line.split(":")
    update[0] = int(update[0])
    update[1] = list(map(int, filter(None, update[1].split(" "))))
    hash[update[0]] = update[1]


def check_hash(target, numbers):
    def helper(current, index):
        if index == len(numbers):
            return current == target
        
        next_number = numbers[index]
 
        return (helper(current + next_number, index + 1) or 
                helper(current * next_number, index + 1) or
                helper(int(str(current) + str(next_number)), index + 1))
    
    return helper(numbers[0], 1)


for key, value in hash.items():
     if check_hash(key, value):
        counter += key

print(counter)