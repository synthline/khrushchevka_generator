from generators.buildings import buildings
from generators.rooms import rooms
from display_2d import display_2d
from loc_calculator import loc_calculator

# Graph origin point: 
univ_origin = (0, 0)

#####__Building Specifcations__##### 
no_areas = 2 ### 0 -- Number of areas per apartment [2,3,4] - this is not including the half:
modular_space = 0 ### 1 -- 0: b_00 (2600x5200), 1: b_10 (combination of b_00 & b_11), 2:b_11(3200x6400): 
rotation = 0 ### 2 -- Geometry rotation (areas are allowed to be formed) 0: linearily, 1: non-linearily:
balconies = 1 ### 3 -- Are balconies included? 0: No, 1: Yes
levels = 1 ### 4 -- Number of levels (without foundation, ground level and roof):
ext_modules = 1 ### 5 -- Number of modules per floor exterior: 0: all the same (if balconies are present, balconies will be prefered instead of windows) 1: some variety ...
apt_modules = 1 ### 6 -- Number of apartment module types per floor interior: 0: all the same (the ones with half are not included here) 1: some variety ...
no_apts = 4 ### 7 -- Number of apartments per floor

# Building Object: 
build_1 = buildings(modular_space)


build_1_loc = loc_calculator(no_areas, modular_space, rotation, balconies, levels, ext_modules, apt_modules, no_apts)
build_1_loc.calculate_apt_and_building_loc()

# Rooms 
rooms_1 = rooms(apt_modules)
rooms_1.get_rooms_and_dims()

# Apartments 
#??

#####__Display__#####
display_1 = display_2d()
