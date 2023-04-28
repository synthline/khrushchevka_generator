import itertools 
import random

class rooms:
    def __init__(self, no_areas, modular_space, apt_modules):
        self.no_areas = no_areas
        self.modular_space = modular_space
        self.apt_modules = apt_modules
        self.essential_room_type_names = ['bathroom', 'kitchen', 'living_room']
        self.essential_room_type_names = ['foyer', 'bedroom_1', 'bedroom_2', 'storage', 'pantry', 'bedroom_3']
        self.room_b00_widths = [1300, 2600, 3900, 5200]
        self.room_b11_widths = [1600, 3200, 4800, 6400]
        self.b_00_room_len = [2600, 3900]
        self.b_11_room_len = [3200, 4800]
        self.rooms = {}
        self.dims = {}

    def generate_room_layouts(number_of_areas):
        pass

         # if area is 2 then bathroom, kitchen, maybe hallway but smallest dimms, living_room
         # if area is 2 then bathroom kitchen, maybe hallway, living_room, bedroom
    def generate_layout_combinations(self):
         # Initialize variables

        number = len(self.essential_room_type_names)
        final_combinations = []
        
        # Use itertools.permutations() to generate all possible permutations
        perms = itertools.permutations(self.essential_room_type_names)
        
        # Convert each permutation tuple to a string and join the characters
        perms_as_strings = [''.join(p) for p in perms]
        for perm in perms_as_strings:   
            final_combinations.append(perm)
        
        # Generate all possible combinations of length equal to the length of the input list
        combinations = [''.join(comb) for comb in itertools.product(self.essential_room_type_names, repeat=number)]
            
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