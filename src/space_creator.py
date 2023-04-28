class space_creator:
    def __init__(self):
        self.space_name = []
        self.points = []
        self.lines = []
        self.space_areas = []
        self.space_comp_dimms = []
        self.space_comp_names = []
        self.total_space_area = 0
        self.no_of_shapes = 0
        self.no_of_spaces = 0

    def generate_space_lines_area(self, dims, name, space_corners):
        space_lines = []
        space_line_names = []
        for i in range(len(space_corners)):
            line = (space_corners[i], space_corners[(i+1)%len(space_corners)])
            space_lines.append(line)
        self.lines.append(space_lines)
        for j in range(len(space_lines)):
            line_name = f"{name}_l{j}"
            space_line_names.append(line_name)
        space_area = dims[0] * dims[1]
        self.space_areas.append(space_area)
        surface_name = f"{name}_s0"
        return space_lines, space_line_names, space_area, surface_name

    def generate_area(self, dict, key, origin_point):
        area_values = []
        area_names = []
        name = key
        self.space_name.append(name)
        dims = dict[name]
        # Defines the center of the space upon which the space coordinates are generated:
        space_center = (origin_point[0] + dims[0]/2, origin_point[1] + dims[1]/2)
         # List of the space corners
        space_corners = [(space_center[0] - dims[0], space_center[1] - dims[1]),
                        (space_center[0], space_center[1] - dims[1]),
                        (space_center[0], space_center[1]),
                        (space_center[0] - dims[0], space_center[1])]
        self.points.append(space_corners)
        # Names the points:
        point_names = []
        for j in range(len(space_corners)):
            point_name = f"{name}_p{j}"
            point_names.append(point_name)
        space_lines, space_line_names, space_area, surface_name = self.generate_space_lines_area(dims, name, space_corners)
        area_values.append((int(name[1]),space_corners, space_lines, space_area))
        area_names.append((name, point_names, space_line_names, surface_name))
        self.space_comp_dimms.append(area_values)
        self.space_comp_names.append(area_names)
        self.no_of_spaces +=1

    def add_area_e(self, dict, key):
        area_values = []
        area_names = []
        name = key
        self.space_name.append(name)
        dims = dict[name]
        starting_point = self.points[self.no_of_spaces -1][1]
        space_center = ((starting_point[0] + dims[0]/2), (starting_point[1] + dims[1])/2) 
        # Define the coordinates of the four corners of the space
        space_corners = [(starting_point),
                        (starting_point[0] + dims[0], starting_point[1]),
                        (starting_point[0] + dims[0], starting_point[1] + dims[1]),
                        (starting_point[0], starting_point[1]+ dims[1])]
        self.points.append(space_corners)
        # Names the points:
        point_names = []
        for j in range(len(space_corners)):
            point_name = f"{name}_p{j}"
            point_names.append(point_name)
        space_lines, space_line_names, space_area, surface_name = self.generate_space_lines_area(dims, name, space_corners)
        area_values.append((int(name[1]),space_corners, space_lines, space_area))
        area_names.append((name, point_names, space_line_names, surface_name))
        self.space_comp_dimms.append(area_values)
        self.space_comp_names.append(area_names)
        self.no_of_spaces +=1
        
    def add_area_w(self, dict, key):
        area_values = []
        area_names = []
        name = key
        self.space_name.append(name)
        dims = dict[name]
        starting_point = self.points[self.no_of_spaces -1][0]
        space_center = ((starting_point[0] + dims[0]/2), (starting_point[1] + dims[1])/2) 
        # Define the coordinates of the four corners of the space
        space_corners = [(starting_point),
                        (starting_point[0] - dims[0], starting_point[1]),
                        (starting_point[0] - dims[0], starting_point[1] + dims[1]),
                        (starting_point[0], starting_point[1] + dims[1])]
        self.points.append(space_corners)
        # Names the points:
        point_names = []
        for j in range(len(space_corners)):
            point_name = f"{name}_p{j}"
            point_names.append(point_name)
        space_lines, space_line_names, space_area, surface_name = self.generate_space_lines_area(dims, name, space_corners)
        area_values.append((int(name[1]),space_corners, space_lines, space_area))
        area_names.append((name, point_names, space_line_names, surface_name))
        self.space_comp_dimms.append(area_values)
        self.space_comp_names.append(area_names)
        self.no_of_spaces +=1

    def add_area_s(self, dict, key):
        area_values = []
        area_names = []
        name = key
        self.space_name.append(name)
        dims = dict[name]
        starting_point = self.points[self.no_of_spaces -1][3]
        space_center = ((starting_point[0] + dims[0]/2), (starting_point[1] + dims[1])/2) 
        # Define the coordinates of the four corners of the space
        space_corners = [(starting_point),
                        (starting_point[0] + dims[0], starting_point[1]),
                        (starting_point[0] + dims[0], starting_point[1] + dims[1]),
                        (starting_point[0], starting_point[1] + dims[1])]
        self.points.append(space_corners)
        # Names the points:
        point_names = []
        for j in range(len(space_corners)):
            point_name = f"{name}_p{j}"
            point_names.append(point_name)
        space_lines, space_line_names, space_area, surface_name = self.generate_space_lines_area(dims, name, space_corners)
        area_values.append((int(name[1]),space_corners, space_lines, space_area))
        area_names.append((name, point_names, space_line_names, surface_name))
        self.space_comp_dimms.append(area_values)
        self.space_comp_names.append(area_names)
        self.no_of_spaces +=1

    def add_area_n(self, dict, key):
        area_values = []
        area_names = []
        name = key
        self.space_name.append(name)
        dims = dict[name]
        starting_point = self.points[self.no_of_spaces -1][0]
        space_center = ((starting_point[0] - dims[0]/2), (starting_point[1] - dims[1])/2) 
        # Define the coordinates of the four corners of the space
        space_corners = [(starting_point[0], starting_point[1] - dims[1]),
                        (starting_point[0] + dims[0], starting_point[1] - dims[1]),
                        (starting_point[0] + dims[0], starting_point[1]),
                        (starting_point)]
        self.points.append(space_corners)
        # Names the points:
        point_names = []
        for j in range(len(space_corners)):
            point_name = f"{name}_p{j}"
            point_names.append(point_name)
        space_lines, space_line_names, space_area, surface_name = self.generate_space_lines_area(dims, name, space_corners)
        area_values.append((int(name[1]),space_corners, space_lines, space_area))
        area_names.append((name, point_names, space_line_names, surface_name))
        self.space_comp_dimms.append(area_values)
        self.space_comp_names.append(area_names)
        self.no_of_spaces +=1

    def generate_combinations(self, dict, key, rotation, origin_point):
        self.generate_area(dict, key, origin_point)
        
        if rotation == 0:
            self.add_area_e(dict, key)

        elif rotation == 1:
            pass

    def generate_rotated_90(self, dict, key, origin_point):
        area_values = []
        area_names = []
        name = key
        self.space_name.append(name)
        temp_dims = dict[name]
        dims = (temp_dims[1], temp_dims[0])
        # Defines the center of the space upon which the space coordinates are generated:
        space_center = (origin_point[0] + dims[0]/2, origin_point[1] + dims[1]/2)
         # List of the space corners
        space_corners = [(space_center[0] - dims[0], space_center[1] - dims[1]),
                        (space_center[0], space_center[1] - dims[1]),
                        (space_center[0], space_center[1]),
                        (space_center[0] - dims[0], space_center[1])]
        self.points.append(space_corners)
        # Names the points:
        point_names = []
        for j in range(len(space_corners)):
            point_name = f"{name}_p{j}"
            point_names.append(point_name)
        space_lines, space_line_names, space_area, surface_name = self.generate_space_lines_area(dims, name, space_corners)
        area_values.append((int(name[1]),space_corners, space_lines, space_area))
        area_names.append((name, point_names, space_line_names, surface_name))
        self.space_comp_dimms.append(area_values)
        self.space_comp_names.append(area_names)
        self.no_of_spaces +=1

    # def add_area_rot_upper_e(self, dict, key):
    #     dims = dict[key]
    #     starting_point = self.points[self.no_of_spaces -1][1]
    #     new_origin_point = starting_point[0] + dims[1]/2, starting_point[0] - dims[1]/2
    #     self.generate_rotated_90(dict, key, new_origin_point)

    # def add_area_rot_lower_e(self, dict, key):
    #     dims = dict[key]
    #     starting_point = self.points[self.no_of_spaces -1][2]
    #     new_origin_point = starting_point[0] - dims[1]/2, starting_point[0] + dims[1]/2
    #     self.generate_rotated_90(dict, key, new_origin_point)

    # def add_area_rot_upper_w(self, dict, key):
    #     dims = dict[key]
    #     starting_point = self.points[self.no_of_spaces -1][3]
    #     space_center = (starting_point[0] - dims[0]/2, starting_point[1] + dims[1]/2)
    #     self.generate_rotated_90(dict, key, starting_point, space_center)

    # def add_area_rot_lower_w(self, dict, key):
    #     dims = dict[key]
    #     starting_point = self.points[self.no_of_spaces -1][2]
    #     space_center = (starting_point[0] - dims[0]/2, starting_point[1] - dims[1]/2)
    #     self.generate_rotated_90(dict, key, starting_point, space_center)

    # def add_area_rot_ne(self, dict, key):
    #     dims = dict[key]
    #     starting_point = self.points[self.no_of_spaces -1][0]
    #     space_center = (starting_point[0] + dims[0]/2, starting_point[1] - dims[1]/2)
    #     self.generate_rotated_90(dict, key, starting_point, space_center)

    # def add_area_rot_nw(self, dict, key):
    #     dims = dict[key]
    #     starting_point = self.points[self.no_of_spaces -1][1]
    #     space_center = (starting_point[0] - dims[0]/2, starting_point[1] - dims[1]/2)
    #     self.generate_rotated_90(dict, key, starting_point, space_center)

    # def add_area_rot_se(self, dict, key):
    #     dims = dict[key]
    #     starting_point = self.points[self.no_of_spaces -1][3]
    #     space_center = (starting_point[0] + dims[0]/2, starting_point[1] + dims[1]/2)
    #     self.generate_rotated_90(dict, key, starting_point, space_center)

    # def add_area_rot_sw(self, dict, key):
    #     dims = dict[key]
    #     starting_point = self.points[self.no_of_spaces -1][2]
    #     space_center = (starting_point[0] - dims[0]/2, starting_point[1] + dims[1]/2)
    #     self.generate_rotated_90(dict, key, starting_point, space_center)

    def generate_shape(self):
        area_values = []
        area_names = []
        name = 'shape' + str(self.no_of_shapes)
        self.space_name.append(name)
        # Initialize a list to hold all coordinates
        all_coords = []
        # Loop over each shape in self.points
        for shapes in self.points:
            for shape in shapes:
                # Check if shape is a tuple
                if isinstance(shape, tuple) and len(shape) == 2:
                    pass
                else:
                    print(f"Invalid shape: {shape}")
                    continue   
                # Add the shape's coordinates to the list
                all_coords.append(shape)
        # Find the minimum and maximum x and y coordinates of all shapes
        x_min = min(all_coords, key=lambda x: x[0])[0]
        x_max = max(all_coords, key=lambda x: x[0])[0]
        y_min = min(all_coords, key=lambda x: x[1])[1]
        y_max = max(all_coords, key=lambda x: x[1])[1]
        # Create a new list of coordinates for the combined shape
        space_corners = [(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_min, y_max)]
        self.points.append(space_corners)
        point_names = []
        for j in range(len(space_corners)):
            point_name = f"{name}_p{j}"
            point_names.append(point_name)
        dims = ((x_max - x_min), (y_max - y_min))
        space_lines, space_line_names, space_area, surface_name = self.generate_space_lines_area(dims, name, space_corners)
        area_values.append((int(name[5]),space_corners, space_lines, space_area))
        area_names.append((name, point_names, space_line_names, surface_name))
        self.space_comp_dimms.append(area_values)
        self.space_comp_names.append(area_names)
        self.no_of_spaces +=1
        self.no_of_shapes +=1

    def generate_total_space(self):
        total_space = 0
        for space in self.space_areas:
            total_space += space
        self.total_space_area = total_space

