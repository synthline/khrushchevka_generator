import itertools
import time

def generate_grid_combinations(x, y, cube_types):
    grid_size = x * y
    combinations = []

    # Generate all possible unique combinations of cube types
    for cube_type_combination in itertools.product(range(cube_types), repeat=grid_size):
        # Convert the grid to a 2D matrix
        matrix = [cube_type_combination[i * x:(i + 1) * x] for i in range(y)]
        
        # Check if the combination is unique and add it to the list
        if matrix not in combinations:
            combinations.append(matrix)

    return combinations


def main():
    x = 3
    y = 4
    cube_types = 4
    
    start_time = time.time()
    combinations = generate_grid_combinations(x, y, cube_types)
    end_time = time.time()
    
    elapsed_time = end_time - start_time

    # Print the number of combinations
    print(f"Total number of combinations: {len(combinations)}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

    # Print the combinations
    # for idx, combo in enumerate(combinations, start=1):
    #     print(f"\nCombination {idx}:")
    #     for row in combo:
    #         print(row)

if __name__ == "__main__":
    main()