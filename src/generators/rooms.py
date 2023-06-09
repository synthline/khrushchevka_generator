import itertools 

class rooms:
    def __init__(self, no_areas, modular_space, apt_modules):
        self.no_areas = no_areas
        self.modular_space = modular_space
        self.apt_modules = apt_modules
        self.essential_room_type_names = ['bathroom', 'kitchen', 'living_room', 'foyer']
        self.additional_room_type_names = ['bedroom_1', 'bedroom_2', 'storage', 'pantry', 'bedroom_3']
        self.room_b00_widths = [1300, 2600, 3900, 5200]
        self.room_b11_widths = [1600, 3200, 4800, 6400]
        self.b_00_room_len = [2600, 3900]
        self.b_11_room_len = [3200, 4800]
        self.room_combinations = []

    def generate_layout_combinations(self):
        # Initialize variables
        list_of_rooms = self.essential_room_type_names
        number = len(list_of_rooms)
        single_combinations = []
        single_combinations = [(elem,) * len(list_of_rooms) for elem in list_of_rooms]
        # Use itertools.permutations() to generate all possible permutations
        perms = itertools.permutations(list_of_rooms)
        # Append each permutation tuple as a 4-element tuple to final_combinations
        for perm in perms:   
            single_combinations.append(tuple(perm) + ("",) * (number - 4))
        # Generate all possible combinations of length equal to the length of the input list
        combinations = [''.join(comb) for comb in itertools.product(list_of_rooms, repeat=number)]           
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
            single_combinations.append(tuple(comb))
        # Creates the tuples of tuples: 
        list_of_tuples = []
        for i in single_combinations:
            for j in single_combinations:
                list_of_tuples.append((i,j))
        print(len(single_combinations))
        # # Filtered tuples, where certain rooms are only allowed to appear once:
        # filtered_list = []
        # for tup in list_of_tuples:
        #     for s in tup:
        #         # Check if the adjacent letters are next to each other and the cornered letter is the last element
        #         if unique_rooms in zip(s, s[1:]):
        #             filtered_list.append(tup)
        #             break
        # self.room_combinations.append(filtered_list)

        
        # # Filtered tuples where we look at the combinations of the rooms are present specifically in some corners:
        # final = [t for t in filtered_list if ((t[0][3] == se_corner and t[1][3] == sw_corner))] 
        # self.room_combinations.append(final)

















































