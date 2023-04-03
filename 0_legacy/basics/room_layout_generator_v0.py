import itertools

def generate_combinations(letters):
    # Initialize variables
    number = len(letters)
    final_combinations = []
    
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


letters = ['a', 'b', 'c', 'd']

result = generate_combinations(letters)
print(result)
print(len(result))




#----------------------BASIC, AND IT WORKS---------------
# import itertools

# def generate_combinations(letters):
#     # Initialize variables
#     number = len(letters)
#     final_combinations = []
    
#     # Generate all possible combinations of length equal to the length of the input list
#     combinations = [''.join(comb) for comb in itertools.product(letters, repeat=number)]
#     return combinations

# letters = ['a', 'b', 'c']
# #letters = ['a', 'b', 'c', 'd']
# result = generate_combinations(letters)
# print(result)
# print(len(result))



# ------------------------------------------------
#def generate_combinations(letters):
#     list_length = len(letters)
#     # 4 of the same --DONE
#     # for i in range(list_length-1):
#     #     yield letters[i] + letters[i] + letters[i] + letters[i] 
#     # 3 of the same case 1
#     # for i in range(list_length-1):
#     #     yield letters[i] + letters[i] + letters[i] + letters[i+1] 
#     # 3 of the same case 2
#     for i in range(list_length-2):
#         yield letters[i] + letters[i] + letters[i] + letters[i+2]
#     # 3 of the same case 1
#     # for i in range(list_length-1):
#     #     yield letters[i] + letters[i] + letters[i] + letters[i+3] 
#     # 3 of the same case 1
#     # for i in range(list_length-1):
#     #     yield letters[i] + letters[i] + letters[i] + letters[i] 



# ----------------------------------
#import itertools

# def generate_combinations(letters):
#     number = len(letters)
#     final_combinations = []

#     # Iterate over all combinations
#     for comb in itertools.product(letters, repeat=number):
#         same_comps = len(set(comb)) == 1
#         has_adjacent = any(comb[i] == comb[i+1] for i in range(number-1))
        
#         has_repeated_alternate = False
#         for i in range(number-2):
#             if comb[i] == comb[i+2]:
#                 has_repeated_alternate = True
#                 break
                
#         if same_comps or (has_adjacent and not has_repeated_alternate):
#             final_combinations.append(''.join(comb))

#     return final_combinations


# --------------------------------------------------
# import itertools

# def generate_combinations(letters):
#     # Initialize variables
#     number = len(letters)
#     final_combinations = []
    
#     # Generate all possible combinations of length equal to the length of the input list
#     combinations = [''.join(comb) for comb in itertools.product(letters, repeat=number)]
    
#     # Add all combinations that contain only the same components
#     for letter in letters:
#         same_comps = letter * len(letters)
#         final_combinations.append(same_comps)
        
#     # Iterate over all combinations
#     for comb in combinations:
#         # Check if the combination has at least two adjacent letters
#         has_adjacent = False
#         for i in range(number-1):
#             if comb[i] == comb[i+1]:
#                 has_adjacent = True
#                 break
#         if not has_adjacent:
#             continue
        
#         # Check if the combination has any repeated letters in alternate positions
#         has_repeated_alternate = False
#         for i in range(0, number-3, 2):
#             if comb[i] == comb[i+2] and comb[i+1] == comb[i+3]:
#                 has_repeated_alternate = True
#                 break
#         if has_repeated_alternate:
#             continue
        
#         # If the combination passes both tests, add it to the final combinations list
#         final_combinations.append(comb)
    
#     return final_combinations


# letters = ['a', 'b', 'c', 'd']

# result = generate_combinations(letters)

# print(result)
# print(len(result))


# list = ['aaaa', 'aaab', 'aaac', 'aaad', 'aabb', 'aabc', 'aabd', 'aacb', 'aacc', 'aacd', 'aadb', 'aadc', 'aadd', 'abbb', 'abbc', 
#  'abbd', 'abcc', 'abdd', 'acbb', 'accb', 'accc', 'accd', 'acdd', 'adbb', 'adcc', 'addb', 'addc', 'addd', 'baaa', 'baac', 
#  'baad', 'bacc', 'badd', 'bbaa', 'bbac', 'bbad', 'bbba', 'bbbb', 'bbbc', 'bbbd', 'bbca', 'bbcc', 'bbcd', 'bbda', 'bbdc', 
#  'bbdd', 'bcaa', 'bcca', 'bccc', 'bccd', 'bcdd', 'bdaa', 'bdcc', 'bdda', 'bddc', 'bddd', 'caaa', 'caab', 'caad', 
#  'cabb', 'cadd', 'cbaa', 'cbba', 'cbbb', 'cbbd', 'cbdd', 'ccaa', 'ccab', 'ccad', 'ccba', 'ccbb', 'ccbd', 'ccca', 'cccb', 
#  'cccc', 'cccd', 'ccda', 'ccdb', 'ccdd', 'cdaa', 'cdbb', 'cdda', 'cddb', 'cddd', 'daaa', 'daab', 'daac', 'dabb', 'dacc', 
#  'dbaa', 'dbba', 'dbbb', 'dbbc', 'dbcc', 'dcaa', 'dcbb', 'dcca', 'dccb', 'dccc', 'dcdd', 'ddaa', 'ddab', 'ddac', 'ddba', 
#  'ddbc', 'ddca', 'ddcb', 'ddcc', 'ddda', 'dddb', 'dddc', 'dddd']

# len = 112
