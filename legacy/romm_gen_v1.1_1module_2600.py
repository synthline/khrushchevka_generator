import itertools

x_len = 2600
y_len = 2400

module = x_len * y_len / 1000000
print(module)

#apts consisting of modules of 4 modules 2x2 

#develop a matrix here and autimatically calculate these len's
max_x_len = x_len * 2 
max_y_len = y_len * 2 

apt_area = 4 * module
print(apt_area)



# import itertools

# # nominal figures:
# widths = [2600, 3200]
# lengths = [1200, 1600, 2400, 3200, 5600]
# apartment_spaces = ['toilet', 'kitchen', 'room', 'hallway']

# #Apt area calculation: (2 * 2600 + 3200) * 5600 / 1000000
# apt_area = 47.04

# #Number of prefab modules an apt is comprised of
# prefab_areas = 3
# prefab_space_length = []

# for width in widths:
#     max_val = max(lengths)
#     prefab_space_length.append(width * max_val / 1000000)

# print(prefab_space_length)



# room_areas = []
# for width in widths:
#     for length in lengths:
#         area = width * length / 1000000
#         room_areas.append(area)

# avg_room_area = sum(room_areas) / len(room_areas)



# # Given the fact that we are designing a studio:
# # if areas can represent all the possible sizes of rooms and thk_areas of the rest of areas,
# # we need to generate all possible combination of studios that contain a room, toilet kitchen and perhaps a hallway
# # that exactly is apt_area in the 3 areas 

# combinations = []


# print(combinations)
