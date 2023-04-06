class buildings:
    def __init__(self, modular_space):
        self.b_id = modular_space
        self.modular_space = modular_space
        self.b_00_building_areas = {'f0': (2600, 5200), 'h0': (1300, 5200)}
        self.b_10_building_areas = {'f1': (2600, 5800), 'f2': (2600, 5800),'f3': (2600, 6400),'f4': (3200, 5200), 'f5': (3200, 5800), 'f6': (3200, 5800),
                                    'h1': (1300, 5800), 'h2': (1300, 5800), 'h3': (1300, 6400), 'h4': (1600, 5200), 'h5': (1600, 5800), 'h6': (1600, 5800)}
        self.b_11_building_areas = {'f7': (3200, 6400), 'h7': (1600, 6400)}
        self.building_types = {0: self.b_00_building_areas, 1: self.b_10_building_areas, 2: self.b_11_building_areas}
        self.building_areas = {}

    def generate_areas(self, number):
        for key, value in self.building_types.items():
            if key == self.b_id:
                dict = value          
                for key in dict:
                    if key.startswith('f'):
                        name = 'f' + str(number * int(key[1]))
                        tuple_value = (number * dict[key][0], dict[key][1])
                        self.building_areas[name] = tuple_value
                    elif key.startswith('h'):
                        key_name = key
                        key_number = int(key[1])
                        for inner_key in list(self.building_areas):
                            if inner_key.startswith('f' + str(number * key_number)):
                                name = str(inner_key) + key_name
                                f_key = 'f' + str(number * key_number)
                                tuple_value = (self.building_areas[f_key][0] + dict[key][0], dict[key][1])
                                self.building_areas[name] = tuple_value

