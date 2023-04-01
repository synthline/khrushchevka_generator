import itertools

# Lengths of area_modules, width_len = max_width
m_len_1 = 2600
m_len_2 = 3200

max_len = (2 * m_len_1) + m_len_2
max_width = 5600

# module_area
max_area = max_len * max_width

# hallway, toilet and kitchen widths
htk = [1200, 1600, 2400]
# room widths
room = [1600, 2400, 3200, 4000, 5600]

rooms_dims_dict = {}
rooms_areas_dict = {}
room_combinations = []

def create_dict(m_len_1, m_len_2, htk, room):
    for i, value in enumerate(htk):
        key_name = f"htk_len1_{i}"
        value_tuple = (m_len_1, value)
        rooms_dims_dict[key_name] = value_tuple
        rooms_areas_dict[key_name] = (value_tuple[0]*value_tuple[1])

        key_name = f"htk_len2_{i}"
        value_tuple = (m_len_2, value)
        rooms_dims_dict[key_name] = value_tuple
        rooms_areas_dict[key_name] = (value_tuple[0]*value_tuple[1])

    for i, value in enumerate(room):
        key_name = f"room_len1_{i}"
        value_tuple = (m_len_1, value)
        rooms_dims_dict[key_name] = value_tuple
        rooms_areas_dict[key_name] = (value_tuple[0]*value_tuple[1])

        key_name = f"room_len2_{i}"
        value_tuple = (m_len_2, value)
        rooms_dims_dict[key_name] = value_tuple
        rooms_areas_dict[key_name] = (value_tuple[0]*value_tuple[1])
    
def generate_area_layouts(rooms_areas_dict, max_area):
    # Create lists of 'htk_' and 'room_' room keys
    htk_rooms = [key for key in rooms_areas_dict.keys() if key.startswith('htk_')]
    room_rooms = [key for key in rooms_areas_dict.keys() if key.startswith('room_')]

    # Create a list of all possible room combinations
    for i in range(3, len(htk_rooms) + 1):
        for j in range(1, len(room_rooms) + 1):
            for htk_combination in itertools.combinations(htk_rooms, i):
                for room_combination in itertools.combinations(room_rooms, j):
                    rooms = list(htk_combination) + list(room_combination)
                    area = sum([rooms_areas_dict[key] for key in rooms])
                    if area <= max_area:
                        room_combinations.append(rooms)
   
###### Bingo Time:

create_dict(m_len_1, m_len_2, htk, room)

generate_area_layouts(rooms_areas_dict, max_area)

print(f"module_area = {max_area / 1000000} m2")

print(f"no_rooms = {len(rooms_dims_dict)}")

# for key, value in rooms_dims_dict.items():
#     print(key + '-' + str(value[0]) + 'x' + str(value[1]))

# for key, value in rooms_areas_dict.items():
#     print(key + '-' + str(value  / 1000000) + ' m2')

print(len(room_combinations))

# for combination in room_combinations:
#     print(combination)

