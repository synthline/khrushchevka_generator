import itertools

# Lengths of area_modules, width_len = max_width
m_len_1 = 2600
max_width = 5600

# module_area
max_area = m_len_1 * max_width

# hallway, toilet and kitchen widths
htk = [1200, 1600, 2400]
# room widths
room = [1600, 2400, 3200, 4000, 5600]

rooms_dims_dict = {}
rooms_areas_dict = {}

def create_dict(m_len_1, htk, room):
    for i, value in enumerate(htk):
        key_name = f"htk_len1_{i}"
        value_tuple = (m_len_1, value)
        rooms_dims_dict[key_name] = value_tuple
        rooms_areas_dict[key_name] = (value_tuple[0]*value_tuple[1])
       
    for i, value in enumerate(room):
        key_name = f"room_len1_{i}"
        value_tuple = (m_len_1, value)
        rooms_dims_dict[key_name] = value_tuple
        rooms_areas_dict[key_name] = (value_tuple[0]*value_tuple[1])

def generate_print_and_count_area_layouts(room_areas_dict, max_area):
    # Create a list of all room keys
    all_rooms = [key for key in room_areas_dict.keys()]

    # Create a set of all possible room combinations
    room_combinations = set()
    for i in range(len(all_rooms) + 1):
        for combination in itertools.combinations(all_rooms, i):
            area = sum([room_areas_dict[key] for key in combination])
            if area <= max_area:
                room_combinations.add(tuple(sorted(combination)))

    # Print all combinations
    for combination in room_combinations:
        print(combination)

    # Count and print the total number of unique combinations
    num_combinations = len(room_combinations)
    print(f"Total number of unique combinations: {num_combinations}")

    # Return the list of unique combinations
    return list(room_combinations)

   
# Generate room dictionaries and combinations
create_dict(m_len_1, htk, room)
combinations = generate_print_and_count_area_layouts(rooms_areas_dict, max_area)

# Print some statistics
print(f"module_area = {max_area / 1000000} m2")
print(f"no_rooms = {len(rooms_dims_dict)}")
print(f"no_combinations = {len(combinations)}")
