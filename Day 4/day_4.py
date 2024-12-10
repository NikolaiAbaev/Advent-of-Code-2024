import re


total_counter = 0
pattern1 = "XMAS"
pattern2 = "SAMX"

### solution for part 2
def count_x_in_matrix(matrix):
    total = 0
    rows, cols = len(matrix), len(matrix[0]) 

    for i in range(1, rows - 1, 1):
        for j in range(1, cols - 1, 1):
            if matrix[i][j] == 'A':
                if (matrix[i - 1][j - 1] == 'M' and  matrix[i + 1][j + 1] == 'S') or (matrix[i - 1][j - 1] == 'S' and  matrix[i + 1][j + 1] == 'M'):
                    if (matrix[i - 1][j + 1] == 'M' and  matrix[i + 1][j - 1] == 'S') or (matrix[i - 1][j + 1] == 'S' and  matrix[i + 1][j - 1] == 'M'):
                        total += 1
    return total


#solution for part 1
def count_pattern_in_matrix(matrix, pattern):
    total = 0
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows - (len(pattern1) - 1)):
        for j in range(cols):
            
            # We always check for a vertical match (edge cases are taken care of by the first for-loop)
            if "".join(matrix[i + k][j] for k in range(4)) == pattern:
                total += 1

            # Diagonal match (top-left to bottom-right)
            if j <= cols - 4:
                if "".join(matrix[i + k][j + k] for k in range(4)) == pattern:
                    total += 1
            # Diagonal match (top-right to bottom-left)
            if j >= 3:
                if "".join(matrix[i + k][j - k] for k in range(4)) == pattern:
                    total += 1
    return total



with open("day_4_data.txt", "r") as file:
    content = file.read()
    # Horizontal matches
    total_counter += len(re.findall(pattern1, content))
    total_counter += len(re.findall(pattern2, content))
    # Convert content to matrix
    matrix = [list(line) for line in content.splitlines()]

# Count patterns in vertical and diagonal directions
total_counter += count_pattern_in_matrix(matrix, pattern1)
total_counter += count_pattern_in_matrix(matrix, pattern2)

print(f'Solution for Part 1 is {total_counter}')
print(f'Solution for Part 2 is {count_x_in_matrix(matrix)}')