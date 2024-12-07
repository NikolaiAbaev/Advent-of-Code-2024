safe_codes = []

with open("data.txt", "r") as file: 
    for line in file:
        strip = line.rstrip().split()
        temp = []
        for i in strip:
            temp.append(int(i))
        
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

