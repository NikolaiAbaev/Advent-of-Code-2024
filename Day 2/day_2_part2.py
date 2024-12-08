#Part II -- Day 2: Red-Nosed Reports
safe_codes = []


def is_safe(list) -> bool:
    if len(list) < 2:
        return True
    
    damper_used = False    

    for i in range(1, len(list)):
        diff = abs(list[i] - list[i - 1])
        
        if diff > 3 or diff == 0:
            if damper_used:
                return False
            damper_used = True
            # [1, 4, 5, 6, 7, 8]
            if abs(list[i] - list[i + 1]) > 3 or abs(list[i] - list[i + 1]) == 0:
                 
            elif abs(list[i - 1] - list[i + 1]):
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
