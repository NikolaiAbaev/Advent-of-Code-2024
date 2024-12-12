def is_in_loop(grid, start_row, start_col):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c, pr, pc, char):
        # If out of bounds or the cell has a different character
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != char:
            return False
        
        # If the cell is already visited and is not the parent, it's a cycle
        if (r, c) in visited:
            return True
        
        # Mark the current cell as visited
        visited.add((r, c))
        
        # Explore all 4 possible directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Skip the parent cell to avoid false positives
            if (nr, nc) != (pr, pc) and dfs(nr, nc, r, c, char):
                return True
        
        return False

    # Start DFS from the given starting position
    return dfs(start_row, start_col, -1, -1, grid[start_row][start_col])

# Example Usage
grid = [
    ['A', 'A', 'B'],
    ['A', 'A', 'B'],
    ['B', 'B', 'B']
]

print(is_in_loop(grid, 0, 0))  # Output: True, as 'A' forms a loop
print(is_in_loop(grid, 2, 0))  # Output: False, as 'B' does not form a loop
