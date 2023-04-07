from display_2d import display_2d
from src.space_creator import space_creator

univ_origin = (0, 0)

#####__Room Types__#####
#room_types = [{'toilet': (26, 13)}]
#areas_rooms = [{'toilet': (26, 13)}, {'bathroom': (26, 13)}, {'kitchen': (26, 16)}, {'hallway': (26, 16)}]
#areas_rooms = [{'toilet': (4, 4)}, {'bathroom': (4, 4)}, {'kitchen': (4, 4)}, {'living_room': (4, 4)}, {'bedroom_1': (4, 4)}, {'bedroom_2': (4, 4)}, {'bedroom_3': (4, 4)}]

temp_dict_of_areas = {'a0': (3200, 6400), 'a1': (3200, 6400)}

apt_1 = space_creator()
apt_1.generate_area(temp_dict_of_areas, 'a0', univ_origin)
apt_1.add_area_rot_ne(temp_dict_of_areas, 'a1')

#####__Display__#####
display_1 = display_2d()
display_1.extract_points(apt_1.space_all)
#display_1.create_and_display_plot()