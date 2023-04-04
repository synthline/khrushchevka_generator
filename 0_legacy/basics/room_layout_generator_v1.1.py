import itertools

def generate_combinations(letters):
    # Initialize variables
    number = len(letters)
    final_combinations = []
    
    final_combinations = [(elem,) * len(letters) for elem in letters]

    # Use itertools.permutations() to generate all possible permutations
    perms = itertools.permutations(letters)

    # Append each permutation tuple as a 4-element tuple to final_combinations
    for perm in perms:   
        final_combinations.append(tuple(perm) + ("",) * (number - 4))

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
            if comb[i] == comb[i+2] and comb[i+1] == comb[i+3]:
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
        final_combinations.append(tuple(comb))

    return final_combinations

def generate_tuples(list):
    list_of_tuples = []
    for i in list:
        for j in list:
            list_of_tuples.append((i,j))
    return list_of_tuples

def filter_tuples(lst, allowed_letters, unique_letters):
    filtered_list = []

    found_letters = {letter: False for letter in unique_letters}
    result = []
    for tup in lst:
        if set(tup) <= allowed_letters:
            for letter in unique_letters:
                if not found_letters[letter] and letter in tup:
                    found_letters[letter] = True
                elif letter in tup:
                    break
            else:
                result.append(tup)
    return result

    # Retrieve all tuples with 4 the same on one side and all different in the other --DONE
    # for t in input_list:
    #     if len(set(t[0])) == 1 and len(set(t[1])) == len(t[1]):
    #         result.append(t)
    # Retrieve all tuples

    # If in one tuple, NOT allowed in another and all 4 must be present



letters = ['a', 'b', 'c', 'd']

result_1 = generate_combinations(letters)
result_2 = generate_tuples(result_1)
result_3 = filter_tuples(result_2)
print(result_3)
print(len(result_3))

#if tuple[0] has 4 letters that are all different then tuple[1] can only have 4 of the same.
#if tuple[1] has 3 letters that are all different then tuple[1] can only have 4th which is not present in the third of the same.
#if tuple[1] has 2 letters that are all different then tuple[1] can only have 2 that are not present in tuple[1].

#in the tuple, 'd' needs to be present either in tuple[1][4], tuple[0][4], tuple[1][0], tuple[0][0]