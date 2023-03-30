import itertools

def generate_grid_combinations(x, y, cubes):
    grid_size = x * y
    combinations = []

    # Generate all possible combinations of cube placements
    for positions in itertools.combinations(range(grid_size), cubes):
        grid = [0] * grid_size
        
        # Set the cube positions in the grid
        for pos in positions:
            grid[pos] = 1
        
        # Convert the grid to a 2D matrix
        matrix = [grid[i * x:(i + 1) * x] for i in range(y)]
        combinations.append(matrix)

    return combinations


def main():
    x = 3
    y = 2
    cubes = 4
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