from itertools import permutations

def generate_layouts(x, y, cubes):
    layouts = []
    
    for combination in permutations(range(cubes + 1), x * y):
        matrix = [list(combination[i * x:(i + 1) * x]) for i in range(y)]
        
        row_sums = [sum(row) for row in matrix]
        if all(row_sum == cubes for row_sum in row_sums):
            layouts.append(matrix)

    print(f'Total number of Combinations: {len(layouts)}')
    for i, layout in enumerate(layouts, 1):
        print(f'\nCombination {i}:')
        for row in layout:
            print(row)

x = 1
y = 2
cubes = 2
generate_layouts(x, y, cubes)

x = 1
y = 3
cubes = 3
generate_layouts(x, y, cubes)

x = 1
y = 4
cubes = 4
generate_layouts(x, y, cubes)