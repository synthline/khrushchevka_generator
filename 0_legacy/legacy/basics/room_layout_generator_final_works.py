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

def filter_tuples(lst, unique_letters):
    result = []
    
    for t in lst:
        counts = {}
        for letter in unique_letters:
            counts[letter] = 0
        
        for sub_tuple in t:
            for letter in sub_tuple:
                if letter in unique_letters:
                    counts[letter] += 1
        
        if all(value == 1 for value in counts.values()):
            result.append(t)
    
    return result

def adjacent_combos(lst, adjacent_letters):
    filtered_list = []
    for tup in lst:
        for s in tup:
            # Check if the adjacent letters are next to each other and the cornered letter is the last element
            if adjacent_letters in zip(s, s[1:]):
                filtered_list.append(tup)
                break
    return filtered_list

def final_combos(lst, se_corner, sw_corner):
    return [t for t in lst if ((t[0][3] == se_corner and t[1][3] == sw_corner))] 


letters = ['a', 'b', 'c', 'd']
unique_letters = ['a', 'b', 'd']
adjacent_letters = ('a', 'b')
se_corner = 'b'
sw_corner = 'd'
result_1 = generate_combinations(letters)
result_2 = generate_tuples(result_1)
#print(len(result_2))
result_3 = filter_tuples(result_2, unique_letters)
result_4 = adjacent_combos(result_3, adjacent_letters)
result_5 = final_combos(result_4, se_corner, sw_corner)
print(result_5)
# print(len(result_5))



