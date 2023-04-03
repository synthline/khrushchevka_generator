import itertools 

class rooms:
    def __init__(self, b_id):
        self.b_id = b_id
        self.room_type_names = ['bathroom', 'kitchen', 'living_room', 'bedroom_1', 'bedroom_2', 'bedroom_3', 'hallway']
        self.b_00_room_dims = []
        self.b_10_room_dims = []
        self.b_11_room_dims = [(1600, 3200), (3200, 3200), (4200, 3200), (4800, 3200), (6400, 3200),
                    (1600, 4800), (3200, 4800), (4200, 4800), (4800, 4800), (6400, 4800)]
        self.building_types = {'b_00': self.b_00_room_dims, 'b_10': self.b_10_room_dims, 'b_11': self.b_11_room_dims}
        self.rooms_and_dims = {}

    # def get_rooms_and_dims(self):
    #         for key, value in self.building_types.items():
    #             if key == self.b_id:
    #                 room_type_sizes = value
    #                 rooms_and_sizes = {f"{name}_{i}": size for i, (name, size) in enumerate(itertools.product(self.room_type_names, room_type_sizes))}
    #                 self.rooms_and_dims = rooms_and_sizes
    #                 print(len(rooms_and_sizes))
    #                 print(rooms_and_sizes)


#we can have an area with 1 room, 2 room, 3 rooms, 4 rooms.
# its easier to generate all combos of rooms and assign their size later

    def generate_room_layouts(number_of_areas):
         # if area is 2 then bathroom, kitchen, maybe hallway but smallest dimms, living_room
         # if area is 2 then bathroom kitchen, maybe hallway, living_room, bedroom
         pass