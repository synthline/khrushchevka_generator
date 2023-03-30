import itertools

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

def generate_grid_combinations(x, y, cubes):
    grid_size = x * y
    valid_combinations = []

    for positions in itertools.combinations(range(grid_size), cubes):
        grid = [0] * grid_size
        
        for pos in positions:
            grid[pos] = 1
        
        matrix = [grid[i * x:(i + 1) * x] for i in range(y)]

        if is_valid(matrix):
            valid_combinations.append(matrix)

    return valid_combinations


def main():
    x = 2
    y = 1
    cubes = 1
    combinations = generate_grid_combinations(x, y, cubes)

    # Print the number of combinations
    print(f"Total possible combinations: {len(combinations)}")

    # Print the combinations
    for idx, combo in enumerate(combinations, start=1):
        print(f"\nCombination {idx}:")
        for row in combo:
            print(row)

if __name__ == "__main__":
    main()   