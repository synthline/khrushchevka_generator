import itertools

def generate_grid_combinations(x, y, cube_types):
    grid_size = x * y
    combinations = []

    # Generate all possible combinations of cube placements
    for positions in itertools.permutations(range(grid_size), grid_size):
        grid = [0] * grid_size

        # Iterate over cube types
        for cube_type_combination in itertools.product(range(cube_types), repeat=grid_size):
            temp_grid = grid.copy()

            # Set the cube positions and types in the grid
            for pos, cube_type in zip(positions, cube_type_combination):
                temp_grid[pos] = cube_type

            # Convert the grid to a 2D matrix
            matrix = [temp_grid[i * x:(i + 1) * x] for i in range(y)]

            # Check if the combination is unique and add it to the list
            if matrix not in combinations:
                combinations.append(matrix)

    return combinations

def main():
    x = 2
    y = 2
    cube_types = 3
    combinations = generate_grid_combinations(x, y, cube_types)

    # Print the number of combinations
    print(f"Total number of combinations: {len(combinations)}")

    # Print the combinations
    for idx, combo in enumerate(combinations, start=1):
        print(f"\nCombination {idx}:")
        for row in combo:
            print(row)

if __name__ == "__main__":
    main()