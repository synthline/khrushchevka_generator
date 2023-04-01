from display_2d import display_2d
from space_creator_v0 import space_creator_v0

univ_origin = (0, 0)

#####__Apartment Areas__#####

#areas_dims = [{'area_0': (26, 56)}]
#areas_dims = [{'area_0': (25, 25)}, {'area_1': (25, 25)} ]
#areas_dims = [{'area_0': (26, 56)}, {'area_1': (32, 56)}, {'area_2': (26, 56)}]

# area_1 = space_creator_v0()
# area_1.horiz_generate_space_all(areas_dims, univ_origin)
#print(area_1.space_all)

# print('\n')

# area_2 = space_creator_v0()
# area_2.vert_generate_space_all(areas_dims, univ_origin)
# print(area_2.space_all)


#####__Apartment Rooms__#####

#areas_rooms = [{'toilet': (26, 13)}]
#areas_rooms = [{'toilet': (26, 13)}, {'bathroom': (26, 13)}, {'kitchen': (26, 16)}, {'hallway': (26, 16)}]
#areas_rooms = [{'toilet': (4, 4)}, {'bathroom': (4, 4)}, {'kitchen': (4, 4)}, {'living_room': (4, 4)}, {'bedroom_1': (4, 4)}, {'bedroom_2': (4, 4)}, {'bedroom_3': (4, 4)}]

# room_1 = space_creator_v0()
# room_1.horiz_generate_space_all(areas_rooms, univ_origin)
# print(room_1.space_all)

# print('\n')

# room_2 = space_creator_v0()
# room_2.vert_generate_space_all(areas_rooms, univ_origin)
# print(room_2.space_all)


#####__Display__#####
# areas_dims = [{'area_0': (25, 25)}]
areas_dims = [{'area_0': (25, 25)}, {'area_1': (25, 25)}, {'area_2': (25, 25)}]
area_1 = space_creator_v0()
area_1.horiz_generate_space_all(areas_dims, univ_origin)

display_1 = display_2d()
display_1.extract_points(area_1.space_all)
display_1.create_and_display_plot()