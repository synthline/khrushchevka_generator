class space_creator_v0:
    def __init__(self):
        self.space_name = []
        self.points = []
        self.lines = []
        self.spaces = []
        self.space_all = []
        self.total_space = 0  

    def horiz_generate_space_all(self, list_of_dims, origin_point):
            #get_space_name(self, list_of_dims):
            for space in list_of_dims:
                for key in space:
                    self.space_name.append(key)
            #generate_points(self, list_of_dims, origin_point):
            endpoint = origin_point
            for i, items in enumerate(list_of_dims):
                for key, value in items.items():
                    # Calculate the coordinates of the space
                    space_center = (endpoint[0] + value[0]/2, endpoint[1] + value[1]/2)
                    # Define the coordinates of the four corners of the space
                    space_corners = [(space_center[0] - value[0]/2, space_center[1] - value[1]/2),
                                    (space_center[0] + value[0]/2, space_center[1] - value[1]/2),
                                    (space_center[0] + value[0]/2, space_center[1] + value[1]/2),
                                    (space_center[0] - value[0]/2, space_center[1] + value[1]/2)]
                    self.points.append(space_corners)
                    endpoint = space_corners[1]
            #generate_lines(self):
            for point_set in self.points:
                lines_list = []
                for i in range(len(point_set)):
                    line = (point_set[i], point_set[(i+1)%len(point_set)])
                    lines_list.append(line)
                self.lines.append(lines_list)
            #generate_surface_space(self, list_of_dims):
            for space in list_of_dims:
                for key, value in space.items():
                    space_surface = value[0] * value[1]
                    self.spaces.append(space_surface)
            #generate_space_data_all(self):
            for i in range(len(self.space_name)):
                space_all_comp = []
                space_all_comp.append(self.space_name[i])
                space_all_comp.extend(self.points[i])
                space_all_comp.extend(self.lines[i])
                space_all_comp.append(self.spaces[i])
                self.space_all.append(space_all_comp)

    def vert_generate_space_all(self, list_of_dims, origin_point):
        #get_space_name(self, list_of_dims):
        for space in list_of_dims:
            for key in space:
                self.space_name.append(key)
        #generate_points(self, list_of_dims, origin_point):
        endpoint = origin_point
        for i, items in enumerate(list_of_dims):
            for key, value in items.items():
                # Calculate the coordinates of the space
                space_center = (endpoint[0] + value[0]/2, endpoint[1] + value[1]/2)
                # Define the coordinates of the four corners of the space
                space_corners = [(space_center[0] - value[0]/2, space_center[1] - value[1]/2),
                                (space_center[0] + value[0]/2, space_center[1] - value[1]/2),
                                (space_center[0] + value[0]/2, space_center[1] + value[1]/2),
                                (space_center[0] - value[0]/2, space_center[1] + value[1]/2)]
                self.points.append(space_corners)
                endpoint = space_corners[3]
        #generate_lines(self):
        for point_set in self.points:
            lines_list = []
            for i in range(len(point_set)):
                line = (point_set[i], point_set[(i+1)%len(point_set)])
                lines_list.append(line)
            self.lines.append(lines_list)
        #generate_surface_space(self, list_of_dims):
        for space in list_of_dims:
            for key, value in space.items():
                space_surface = value[0] * value[1]
                self.spaces.append(space_surface)
        #generate_space_data_all(self):
        for i in range(len(self.space_name)):
            space_all_comp = []
            space_all_comp.append(self.space_name[i])
            space_all_comp.extend(self.points[i])
            space_all_comp.extend(self.lines[i])
            space_all_comp.append(self.spaces[i])
            self.space_all.append(space_all_comp)

    def generate_total_space(self):
        total_space = 0
        for space in self.spaces:
            total_space += space
        self.total_space = total_space


    # The same as the above, but fragmented into several functions

    def get_space_name(self, list_of_dims):
        for space in list_of_dims:
            for key in space:
                self.space_name.append(key)

    def horiz_generate_points(self, list_of_dims, origin_point):
        endpoint = origin_point
        for i, items in enumerate(list_of_dims):
            for key, value in items.items():
                # Calculate the coordinates of the space
                space_center = (endpoint[0] + value[0]/2, endpoint[1] + value[1]/2)
                # Define the coordinates of the four corners of the space
                space_corners = [(space_center[0] - value[0]/2, space_center[1] - value[1]/2),
                                 (space_center[0] + value[0]/2, space_center[1] - value[1]/2),
                                 (space_center[0] + value[0]/2, space_center[1] + value[1]/2),
                                 (space_center[0] - value[0]/2, space_center[1] + value[1]/2)]
                self.points.append(space_corners)
                endpoint = space_corners[1]

    def vert_generate_points(self, list_of_dims, origin_point):
        endpoint = origin_point
        for items in list_of_dims:
            for key, value in items.items():
                # Calculate the coordinates of the space
                space_center = (endpoint[0] + value[0]/2, endpoint[1] + value[1]/2)
                # Define the coordinates of the four corners of the space
                space_corners = [(space_center[0] - value[0]/2, space_center[1] - value[1]/2),
                                 (space_center[0] + value[0]/2, space_center[1] - value[1]/2),
                                 (space_center[0] + value[0]/2, space_center[1] + value[1]/2),
                                 (space_center[0] - value[0]/2, space_center[1] + value[1]/2)]
                self.points.append(space_corners)
                endpoint = space_corners[3]

    def generate_lines(self):
        for point_set in self.points:
            lines_list = []
            for i in range(len(point_set)):
                line = (point_set[i], point_set[(i+1)%len(point_set)])
                lines_list.append(line)
            self.lines.append(lines_list)

    def generate_surface_space(self, list_of_dims):
        for space in list_of_dims:
            for key, value in space.items():
                space_surface = value[0] * value[1]
                self.spaces.append(space_surface)

    def generate_space_data_all(self):
        for i in range(len(self.space_name)):
            space_all_comp = []
            space_all_comp.append(self.space_name[i])
            space_all_comp.extend(self.points[i])
            space_all_comp.extend(self.lines[i])
            space_all_comp.append(self.spaces[i])
            self.space_all.append(space_all_comp)
