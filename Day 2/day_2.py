#Part I -- Day 2: Red-Nosed Reports

safe_codes = []
all_codes = []

with open("data.txt", "r") as file: 
    for line in file:
        strip = line.rstrip().split()
        temp = []
        for i in strip:
            temp.append(int(i))

        #adding all codes here for part II
        all_codes.append(temp)
        
        safe = True
        if temp[0] - temp[1] > 0:
            increasing = False
        else:
            increasing = True

        for i in range(1, len(temp), 1):
            if abs(temp[i - 1] - temp[i]) > 3 or abs(temp[i - 1] - temp[i]) < 1:
                safe = False
                break

            if (increasing == True and temp[i - 1] - temp[i] > 0) or (increasing == False and temp[i - 1] - temp[i] < 0):
                safe = False
                break
        
        if safe == True:
            safe_codes.append(temp)

answer = len(safe_codes)
print(f'{answer} Codes are Safe')

#Part II 
safe_codes_part_two = []
print(all_codes)
for code in all_codes:
    damper = False 
    safe = True
    if code[0] - code[1] > 0:
        increasing = False
    else:
        increasing = True

    for i in range(1, len(code), 1):
        print(i)
        if abs(code[i - 1] - code[i]) > 3 or abs(code[i - 1] - code[i]) < 1:
            if damper == True:
                damper = False
                i += 2
            else:
                safe = False
                break

        if (increasing == True and code[i - 1] - code[i] > 0) or (increasing == False and code[i - 1] - code[i] < 0):
            if damper == True:
                damper = False
            else:
                safe = False
                break

    if safe == True:
        safe_codes_part_two.append(code)

print(len(safe_codes))