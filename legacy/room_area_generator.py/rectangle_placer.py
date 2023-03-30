from itertools import combinations, product

def generate_rectangular_grid_combinations(rectangles, num_cuboids):
    grid_height = len(rectangles)
    grid_width = max(width for _, width in rectangles)
    grid_size = sum(height * width for height, width in rectangles)
    
    grid_combinations = []

    for combination in combinations(range(grid_size), num_cuboids):
        grid = [[0] * grid_width for _ in range(grid_height)]
        
        for idx in combination:
            row, col = divmod(idx, grid_width)
            if col < rectangles[row][1]:
                grid[row][col] = 1

        if is_valid(grid):
            grid_combinations.append(grid)

    return grid_combinations

def is_valid(matrix):
    def is_adjacent(row, col):
        adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for r, c in adjacent_positions:
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == 1:
                return True
        return False

    cubes_positions = [(row, col) for row in range(len(matrix)) for col in range(len(matrix[0])) if matrix[row][col] == 1]
    visited = set()

    def dfs(row, col):
        if (row, col) in visited or not (0 <= row < len(matrix)) or not (0 <= col < len(matrix[0])) or matrix[row][col] == 0:
            return

        visited.add((row, col))
        adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for r, c in adjacent_positions:
            dfs(r, c)

    start_row, start_col = cubes_positions[0]
    dfs(start_row, start_col)

    return len(visited) == len(cubes_positions)

# Example usage:
rectangles = [(2, 3), (2, 3)]  # 2 rows, each with 3 columns
num_cuboids = 4
combinations = generate_rectangular_grid_combinations(rectangles, num_cuboids)

for i, combination in enumerate(combinations, 1):
    print(f"Combination {i}:")
    for row in combination:
        print(row)
    print()