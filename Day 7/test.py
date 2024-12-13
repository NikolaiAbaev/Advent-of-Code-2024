def can_reach_target(target, numbers):
    def helper(current, index):
        # Base case: If we've used all numbers, check if we reached the target
        if index == len(numbers):
            return current == target
        
        # Get the next number
        next_number = numbers[index]
        
        # Explore both addition and multiplication
        return (helper(current + next_number, index + 1) or
                helper(current * next_number, index + 1))
    
    # Start recursion with the first number and index 1
    return helper(numbers[0], 1)

# Example
target = 2371 
numbers = [8, 5, 10, 74, 611, 58]

result = can_reach_target(target, numbers)
print("Can reach target:", result)
