#Part II -- Day 2: Red-Nosed Reports
safe_codes = []
badone = [67, 66, 68, 70, 71, 74, 76]

def is_safe(list) -> bool:
    if len(list) < 2:
        return True
    left, right = 0, 1
    damper_used = False    

    increasing = list[left] + list[left + 1] < list[right + 1] + list[right + 2]

    while right < len(list):
        diff = list[right] - list[left]
        
        if abs(diff) > 3 or abs(diff) == 0 or (increasing and diff <= 0) or (not increasing and diff >= 0):
            if damper_used:
                return False
            damper_used = True

            if right < len(list) - 1:
                if (abs(list[right] - list[right + 1]) < 4 and abs(list[right] - list[right + 1]) != 0):
                    if (increasing and (list[right] - list[right + 1]) < 0) or (not increasing and (list[right] - list[right + 1]) > 0):
                        right += 2
                        left += 2
                elif abs(list[left] - list[right + 1]) < 4 and abs(list[left] - list[right + 1] != 0):
                    if (increasing and (list[left] - list[right + 1]) < 0) or (not increasing and (list[left] - list[right + 1]) > 0):    
                        right += 2
                        left += 2
                else:
                    return False
            else:
                return True
        else:
            left += 1
            right += 1

    return True

print(is_safe(badone))