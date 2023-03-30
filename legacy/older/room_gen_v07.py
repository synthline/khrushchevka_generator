import itertools
import matplotlib.pyplot as plt

# Lengths of area_modules, width_len = max_width
m_len_1 = 2600
max_width = 5600
max_len = m_len_1  # define max_len based on m_len_1

# module_area
max_area = max_len * max_width

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

# Plot the room combinations
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim([0, max_width])
ax.set_ylim([0, max_len])

for combination in combinations:
    x = 1
    y = 1
    for room_key in combination:
        room_dims = rooms_dims_dict[room_key]
        rect = plt.Rectangle((x, y), room_dims[1], room_dims[0], edgecolor='black', facecolor='none')
        ax.add_patch(rect)
        x += room_dims[1]
    y += max(room_dims)

plt.show()
