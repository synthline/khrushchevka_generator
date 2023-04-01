import itertools

def generate_grid_combinations(x, y, cube_types):
    grid_size = x * y
    combinations = []

    # Generate all possible unique combinations of cube placements
    for cube_type_combination in itertools.permutations(range(1, cube_types + 1), grid_size):
        # Convert the grid to a 2D matrix
        matrix = [list(cube_type_combination[i * x:(i + 1) * x]) for i in range(y)]

        # Check if the combination is unique and add it to the list
        if matrix not in combinations:
            combinations.append(matrix)

    return combinations

def main():
    x = 3
    y = 3
    cube_types = 6
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
