import itertools

def generate_combinations(letters):
    # Initialize variables
    number = len(letters)
    final_combinations = []

    # Simple loop to generate all values with all 4 chars that are the same:
    for elem in letters:
        final_combinations.append(elem * number)
    
    # Use itertools.permutations() to generate all possible permutations
    perms = itertools.permutations(letters)
    
    # Convert each permutation tuple to a string and join the characters
    perms_as_strings = [''.join(p) for p in perms]
    for perm in perms_as_strings:   
        final_combinations.append(perm)
    
    # Generate all possible combinations of length equal to the length of the input list
    combinations = [''.join(comb) for comb in itertools.product(letters, repeat=number)]
        
    # Iterate over all combinations
    for comb in combinations:
        # Check if the combination has at least two adjacent letters
        has_adjacent = False
        for i in range(number-1):
            if comb[i] == comb[i+1]:
                has_adjacent = True
                break
        if not has_adjacent:
            continue
        
        # Check if the combination has any repeated letters in alternate positions #1
        has_repeated_alternate = False
        for i in range(0, number-3, 2):
            if comb[i] == comb[i+2] and comb[i+1] == comb[i+3]:##
                has_repeated_alternate = True
                break
        if has_repeated_alternate:
            continue

        # Check if the combination has any repeated letters in alternate positions #2
        has_repeated_alternate = False
        for i in range(0, number-3, 2):
            if comb[i] == comb[i+1] and comb[i+1] == comb[i+3]:
                has_repeated_alternate = True
                break
        if has_repeated_alternate:
            continue
        
        # Check if the combination has any repeated letters in alternate positions #3
        has_repeated_alternate = False
        for i in range(0, number-3, 2):
            if comb[i] == comb[i+2] and comb[i+2] == comb[i+3]:
                has_repeated_alternate = True
                break
        if has_repeated_alternate:
            continue

        # Check if the combination has any repeated letters in alternate positions #4
        has_repeated_alternate = False
        for i in range(0, number-3, 2):
            if comb[i] == comb[i+3] and comb[i+1] == comb[i+2]:
                has_repeated_alternate = True
                break
        if has_repeated_alternate:
            continue

        # If the combination passes all 4 tests, add it to the final combinations list
        final_combinations.append(comb)
    
    return final_combinations

def generate_tuples(list):
    list_of_tuples = []
    for i in list:
        for j in list:
            list_of_tuples.append((i,j))
    return list_of_tuples

letters = ['a', 'b', 'c', 'd']

result_1 = generate_combinations(letters)
print(result_1)
print(len(result_1))

result_2 = generate_tuples(result_1)
print(result_2)
print(len(result_2))
