#Part II -- Day 2: Red-Nosed Reports
safe_codes = []


def is_safe(list) -> bool:
    if len(list) < 2:
        return True
    left, right = 0, 1
    damper_used = False    

    while right < len(list):
        diff = abs(list[right] - list[left])
        
        if diff > 3 or diff == 0:
            if damper_used:
                return False
            damper_used = True
            # [1, 4, 5, 6, 7, 8]
            if (abs(list[right] - list[right + 1]) < 4 and abs(list[right] - list[right + 1]) != 0):
                right += 2
                left += 2
            elif abs(list[left] - list[right + 1]):
                do 
            else:
                return False 


    return True
        


with open("data.txt", "r") as file: 
    for line in file:
        strip = line.rstrip().split()
        temp = []
        for i in strip:
            temp.append(int(i))
        
        if is_safe(temp) == True:
            safe_codes.append(temp)

print(len(safe_codes))
