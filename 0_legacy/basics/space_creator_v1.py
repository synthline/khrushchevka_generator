class space_creator:
    def __init__(self):
        self.new_origin_point = ()
        self.space_name = []
        self.points = []
        self.lines = []
        self.spaces = []
        self.space_all = []
        self.space_names_all = []
        self.total_space = 0
        
    def generate_area(self, dict_of_dims, origin_point):
        points = []
        space_all = []
        space_names_all = []
        
        for name, dims in dict_of_dims.items():
            space_center = (origin_point[0] + dims[0]/2, origin_point[1] + dims[1]/2)
            space_corners = [(space_center[0] - dims[0], space_center[1] - dims[1]),
                            (space_center[0], space_center[1] - dims[1]),
                            (space_center[0], space_center[1]),
                            (space_center[0] - dims[0], space_center[1])]
            space_points = space_corners
            space_lines = []
            for i in range(len(space_points)):
                line = (space_points[i], space_points[(i+1)%len(space_points)])
                space_lines.append(line)
            space_area = dims[0] * dims[1]
            space_data = [name]
            space_data.extend(space_points)
            space_data.extend(space_lines)
            space_data.append(space_area)
            space_names = [name]
            for j in range(len(space_points)):
                point_name = f"{name}_p{j}"
                space_names.append(point_name)
            for j in range(len(space_lines)):
                line_name = f"{name}_l{j}"
                space_names.append(line_name)
            surface_name = f"{name}_s0"
            space_names.append(surface_name)
            
            points.append(space_points)
            space_all.append(space_data)
            space_names_all.append(space_names)
        # update the class variables
        self.space_name.extend(list(dict_of_dims.keys()))
        self.points.extend(points)
        self.lines.extend(space_lines)
        self.spaces.extend([dims[0] * dims[1] for dims in dict_of_dims.values()])
        self.space_all.extend(space_all)
        self.space_names_all.extend(space_names_all)

    def rotate(self, list_of_dims, origin_point):
        for space_name, dimensions in list_of_dims.items():
            # Add the space name to the list
            self.space_name.append(space_name)
            # Calculate the coordinates of the space
            space_center = (origin_point[0] + dimensions[0]/2, origin_point[1] + dimensions[1]/2)
            # Define the coordinates of the four corners of the space
            space_corners = [(space_center[0] - dimensions[1]/2, space_center[1]- dimensions[0]/2),
                            (space_center[0] + dimensions[1]/2, space_center[1] - dimensions[0]/2),
                            (space_center[0] + dimensions[1]/2, space_center[1] + dimensions[1]/2),
                            (space_center[0] - dimensions[1]/2, space_center[1] + dimensions[1]/2)]
            self.points.append(space_corners)
            # Generate lines connecting the points
            lines_list = []
            for i in range(len(space_corners)):
                line = (space_corners[i], space_corners[(i+1)%len(space_corners)])
                lines_list.append(line)
            self.lines.append(lines_list)
            # Calculate the surface area of the space
            space_surface = dimensions[0] * dimensions[1]
            self.spaces.append(space_surface)
            # Add all the space data to the space_all list
            space_all_comp = []
            space_all_comp.append(space_name)
            space_all_comp.extend(space_corners)
            space_all_comp.extend(lines_list)
            space_all_comp.append(space_surface)
            self.space_all.append(space_all_comp)
            # Add all the space names to the space_names_all list
            names_list = [space_name]
            for j in range(len(space_corners)):
                point_name = f"{space_name}_p{j}"
                names_list.append(point_name)
            for j in range(len(lines_list)):
                line_name = f"{space_name}_l{j}"
                names_list.append(line_name)
            surface_name = f"{space_name}_s0"
            names_list.append(surface_name)
            self.space_names_all.append(names_list)


    def add_area_e(self, list_of_dims, origin_point):
        for space_name, dimensions in list_of_dims.items():
            # Add the space name to the list
            self.space_name.append(space_name)
            # Calculate the coordinates of the space
            space_center = (origin_point[0] + dimensions[0]/2, origin_point[1] + dimensions[1]/2)
            # Define the coordinates of the four corners of the space
            space_corners = [(space_center[0] - dimensions[0]/2, space_center[1] - dimensions[1]/2),
                            (space_center[0] + dimensions[0]/2, space_center[1] - dimensions[1]/2),
                            (space_center[0] + dimensions[0]/2, space_center[1] + dimensions[1]/2),
                            (space_center[0] - dimensions[0]/2, space_center[1] + dimensions[1]/2)]
            self.points.append(space_corners)
            # Generate lines connecting the points
            lines_list = []
            for i in range(len(space_corners)):
                line = (space_corners[i], space_corners[(i+1)%len(space_corners)])
                lines_list.append(line)
            self.lines.append(lines_list)
            # Calculate the surface area of the space
            space_surface = dimensions[0] * dimensions[1]
            self.spaces.append(space_surface)
            # Add all the space data to the space_all list
            space_all_comp = []
            space_all_comp.append(space_name)
            space_all_comp.extend(space_corners)
            space_all_comp.extend(lines_list)
            space_all_comp.append(space_surface)
            self.space_all.append(space_all_comp)
            # Add all the space names to the space_names_all list
            names_list = [space_name]
            for j in range(len(space_corners)):
                point_name = f"{space_name}_p{j}"
                names_list.append(point_name)
            for j in range(len(lines_list)):
                line_name = f"{space_name}_l{j}"
                names_list.append(line_name)
            surface_name = f"{space_name}_s0"
            names_list.append(surface_name)
            self.space_names_all.append(names_list)

    def add_area_w(self, list_of_dims, origin_point):
        for space_name, dimensions in list_of_dims.items():
            # Add the space name to the list
            self.space_name.append(space_name)
            # Calculate the coordinates of the space
            space_center = (origin_point[0] + dimensions[0]/2, origin_point[1] + dimensions[1]/2)
            # Define the coordinates of the four corners of the space
            space_corners = [(space_center[0] - (dimensions[0]/2 + dimensions[0]), space_center[1] - dimensions[1]/2),
                            (space_center[0] - dimensions[0]/2, space_center[1] - dimensions[1]/2),
                            (space_center[0] - dimensions[0]/2, space_center[1] + dimensions[1]/2),
                            (space_center[0] - (dimensions[0]/2 + dimensions[0]), space_center[1] + dimensions[1]/2)]
            self.points.append(space_corners)
            # Generate lines connecting the points
            lines_list = []
            for i in range(len(space_corners)):
                line = (space_corners[i], space_corners[(i+1)%len(space_corners)])
                lines_list.append(line)
            self.lines.append(lines_list)
            # Calculate the surface area of the space
            space_surface = dimensions[0] * dimensions[1]
            self.spaces.append(space_surface)
            # Add all the space data to the space_all list
            space_all_comp = []
            space_all_comp.append(space_name)
            space_all_comp.extend(space_corners)
            space_all_comp.extend(lines_list)
            space_all_comp.append(space_surface)
            self.space_all.append(space_all_comp)
            # Add all the space names to the space_names_all list
            names_list = [space_name]
            for j in range(len(space_corners)):
                point_name = f"{space_name}_p{j}"
                names_list.append(point_name)
            for j in range(len(lines_list)):
                line_name = f"{space_name}_l{j}"
                names_list.append(line_name)
            surface_name = f"{space_name}_s0"
            names_list.append(surface_name)
            self.space_names_all.append(names_list)

    def add_area_s(self, list_of_dims, origin_point):
        for space_name, dimensions in list_of_dims.items():
            # Add the space name to the list
            self.space_name.append(space_name)
            # Calculate the coordinates of the space
            space_center = (origin_point[0] + dimensions[0]/2, origin_point[1] + dimensions[1]/2)
            # Define the coordinates of the four corners of the space
            space_corners = [(space_center[0] - dimensions[0]/2, space_center[1] + dimensions[1]/2),
                            (space_center[0] + dimensions[0]/2, space_center[1] + dimensions[1]/2),
                            (space_center[0] + dimensions[0]/2, space_center[1] + dimensions[1]/2 + dimensions[1]),
                            (space_center[0] - dimensions[0]/2, space_center[1] + (dimensions[1]/2) + dimensions[1])]
            self.points.append(space_corners)
            # Generate lines connecting the points
            lines_list = []
            for i in range(len(space_corners)):
                line = (space_corners[i], space_corners[(i+1)%len(space_corners)])
                lines_list.append(line)
            self.lines.append(lines_list)
            # Calculate the surface area of the space
            space_surface = dimensions[0] * dimensions[1]
            self.spaces.append(space_surface)
            # Add all the space data to the space_all list
            space_all_comp = []
            space_all_comp.append(space_name)
            space_all_comp.extend(space_corners)
            space_all_comp.extend(lines_list)
            space_all_comp.append(space_surface)
            self.space_all.append(space_all_comp)
            # Add all the space names to the space_names_all list
            names_list = [space_name]
            for j in range(len(space_corners)):
                point_name = f"{space_name}_p{j}"
                names_list.append(point_name)
            for j in range(len(lines_list)):
                line_name = f"{space_name}_l{j}"
                names_list.append(line_name)
            surface_name = f"{space_name}_s0"
            names_list.append(surface_name)
            self.space_names_all.append(names_list)

    def add_area_n(self, list_of_dims, origin_point):
        for space_name, dimensions in list_of_dims.items():
            # Add the space name to the list
            self.space_name.append(space_name)
            # Calculate the coordinates of the space
            space_center = (origin_point[0] + dimensions[0]/2, origin_point[1] + dimensions[1]/2)
            # Define the coordinates of the four corners of the space
            space_corners = [(space_center[0] - dimensions[0]/2, space_center[1] - (dimensions[1]/2 + dimensions[1])),
                            (space_center[0] + dimensions[0]/2, space_center[1] - (dimensions[1]/2 + dimensions[1])),
                            (space_center[0] + dimensions[0]/2, space_center[1] - dimensions[1]/2),
                            (space_center[0] - dimensions[0]/2, space_center[1] - dimensions[1]/2)]
            self.points.append(space_corners)
            # Generate lines connecting the points
            lines_list = []
            for i in range(len(space_corners)):
                line = (space_corners[i], space_corners[(i+1)%len(space_corners)])
                lines_list.append(line)
            self.lines.append(lines_list)
            # Calculate the surface area of the space
            space_surface = dimensions[0] * dimensions[1]
            self.spaces.append(space_surface)
            # Add all the space data to the space_all list
            space_all_comp = []
            space_all_comp.append(space_name)
            space_all_comp.extend(space_corners)
            space_all_comp.extend(lines_list)
            space_all_comp.append(space_surface)
            self.space_all.append(space_all_comp)
            # Add all the space names to the space_names_all list
            names_list = [space_name]
            for j in range(len(space_corners)):
                point_name = f"{space_name}_p{j}"
                names_list.append(point_name)
            for j in range(len(lines_list)):
                line_name = f"{space_name}_l{j}"
                names_list.append(line_name)
            surface_name = f"{space_name}_s0"
            names_list.append(surface_name)
            self.space_names_all.append(names_list)


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