from collections import Counter
import itertools

#####__Area Types__#####

areas = [{'f0': (2600, 5200)}, {'f1': (2600, 5800)}, {'f2': (2600, 5800)}, {'f3': (2600, 6400)}, 
              {'f4': (3200, 5200)}, {'f5': (3200, 5800)}, {'f6': (3200, 5800)}, {'f7': (3200, 6400)}, 
              {'h0': (2600, 5200)}, {'h1': (2600, 5800)}, {'h2': (2600, 5800)}, {'h3': (2600, 6400)}, 
              {'h4': (3200, 5200)}, {'h5': (3200, 5800)}, {'h6': (3200, 5800)}, {'h7': (3200, 6400)}]

area_types = [{'f0': (2600, 5200)}, {'f1': (2600, 5800)}, {'f2': (2600, 5800)}, {'f3': (2600, 6400)}, 
              {'f4': (3200, 5200)}, {'f5': (3200, 5800)}, {'f6': (3200, 5800)}, {'f7': (3200, 6400)}] 


def generate_combinations(area_types, width):
    letters = [area_type.keys()[0] for area_type in area_types]
    combinations = []
    for i in range(1, width + 1):
        for combination in itertools.product(letters, repeat=i):
            counts = Counter(combination)
            if len(counts) == 1 and area_types[letters.index(combination[0])][combination[0]][0] == width:
                new_key = ''.join([key for key in counts.keys()]) + str(width)
                new_value = area_types[letters.index(combination[0])][combination[0]]
                combinations.append({new_key: new_value})
    return combinations

width = 5200
combinations = generate_combinations(area_types, width)
print(combinations)

















# def generate_combinations(letters, number):
#     if number == 0:
#         return ['']
#     result = []
#     for letter in letters:
#         if number > 1:
#             for combination in generate_combinations(letters, number - 1):
#                 result.append(letter + combination)
#         else:
#             result.append(letter)
#     return result

# letters = ['a', 'b', 'c']
# number = 2
# combinations = generate_combinations(letters, number)
# print(combinations)
# print(len(combinations))
