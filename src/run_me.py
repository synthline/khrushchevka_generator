from generators.buildings import buildings
from generators.rooms import rooms
from display_2d import display_2d


# Graph origin point: 
univ_origin = (0, 0)
building_type = 'b_11'

# Building
build_1 = buildings(building_type)
build_1.generate_areas(2)
print(build_1.building_areas)

# Rooms
rooms_1 = rooms(building_type)
rooms_1.get_rooms_and_dims()


#####__Display__#####
display_1 = display_2d()
