from generators.buildings import buildings
from generators.rooms import rooms
from display_2d import display_2d
from loc_calculator import loc_calculator
from space_creator import space_creator

# Graph origin point: 
# univ_origin = (0, 0)

#####__Building Specifcations__##### 
no_areas = 2 ### 0 -- Number of areas per apartment [2,3,4] - this is not including the half:
modular_space = 2 ### 1 -- 0: b_00 (2600x5200), 1: b_10 (combination of b_00 & b_11), 2:b_11(3200x6400): 
rotation = 0 ### 2 -- Geometry rotation (areas are allowed to be formed) 0: linearily, 1: non-linearily:
balconies = 1 ### 3 -- Are balconies included? 0: No, 1: Yes
levels = 1 ### 4 -- Number of levels (without foundation, ground level and roof):
ext_modules = 1 ### 5 -- Number of modules per floor exterior: 0: all the same (if balconies are present, balconies will be prefered instead of windows) 1: some variety ...
apt_modules = 1 ### 6 -- Number of apartment module types per floor interior: 0: all the same (the ones with half are not included here) 1: some variety ...
no_apts = 4 ### 7 -- Number of apartments per floor

# Building Object: ---------------------NOT SURE WHAT IS THE USE OF THIS ANYMORE----PLS REVIEW.
building_1 = buildings(modular_space)
building_1.generate_areas(no_areas)

# Building LOC:
# build_1_loc = loc_calculator(no_areas, modular_space, rotation, levels, ext_modules, apt_modules, no_apts)
# build_1_loc.calculate_apt_and_building_loc()
# print(build_1_loc.apt_loc_score)
# print(build_1_loc.building_loc_score)

# Room Layout Generator:
#rooms_1 = rooms(no_areas, modular_space, apt_modules)


# Temp graph origin point: 
univ_origin = (0, 0)
temp_areas = {'a0': (3200, 6400), 'a1': (4000, 6400)} # This will be an utput from building_1
staircase = {'s0': (3200, 6400)}

# Instantiate the areas:
apt_1 = space_creator()
apt_2 = space_creator()
stairs_0 = space_creator()
levels = space_creator()


apt_1.generate_area(temp_areas, 'a0', univ_origin)
apt_1.add_area_e(temp_areas, 'a0')

# apt_1.generate_combinations(temp_areas, 'a0', rotation)
# apt_2.generate_combinations(temp_areas, 'a1', rotation)

# levels.generate_apt_combinations(apt_1, apt_2, stairs_0, no_apts)


# #####__Display__#####
display_1 = display_2d()
display_1.extract_points(apt_1.points)
display_1.create_and_display_plot()