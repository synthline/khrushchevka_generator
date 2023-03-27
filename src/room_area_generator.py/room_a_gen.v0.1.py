import itertools

origin =  (0,0,0)
#Per Floor:
#later iteration:
#apartment_spaces = ['toilet', 'kitchen', 'room', 'l_room', 'b_room', 'hallway']

#apartment_spaces = ['toilet', 'kitchen', 'room', 'hallway']
# An apartment has to have as a minimum a toilet, kitchen and room.


import itertools

widths = [2325, 3050]
lengths = [988, 1450, 2125, 3050, 5325]
apartment_spaces = ['toilet', 'kitchen', 'room', 'hallway']
max_apartment_size = (5700, 5325)

combinations = [(width, length) for width in widths for length in lengths]

apt_combinations = {}

for i in range(1, len(combinations) + 1):
    for combination in itertools.combinations(combinations, i):
        # Initialize the apartment combination with the hallway as the smallest space
        apt_comb = [('hallway', min(combinations))]
        remaining_spaces = [space for space in apartment_spaces if space != 'hallway']
        remaining_combinations = [comb for comb in combination if comb != min(combinations)]
        
        # Add the kitchen and toilets with medium-sized combinations
        for space in ['kitchen', 'toilet']:
            if remaining_combinations:
                medium_comb = max(remaining_combinations)
                remaining_combinations.remove(medium_comb)
                apt_comb.append((space, medium_comb))
        
        # Add the remaining spaces with the largest available combination
        for space in remaining_spaces:
            if remaining_combinations:
                large_comb = max(remaining_combinations)
                remaining_combinations.remove(large_comb)
                apt_comb.append((space, large_comb))
        
        # Construct the apartment combination string and add it to the dictionary
        apt_comb_str = ', '.join([f"{space}: {comb[0]}x{comb[1]}" for space, comb in apt_comb])
        apt_combinations[apt_comb_str] = apt_comb

# Generate all possible combinations of apartments based on the apartment combinations




        
# room_areas = cross-product of these 2 lists.

# make line_coordinates:
# widths will go on y_axis, lengths on x_axis