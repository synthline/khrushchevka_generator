class space_creator:
    def __init__(self):
        self.space_name = []
        self.points = []
        self.lines = []
        self.spaces = []
        self.space_all = []
        self.space_names_all = []
        self.total_space = 0
        self.total_spaces = 0
        self.shape_no = 0

    def generate_shape(self):
        name = 'shape' + str(self.shape_no)
        points = []
        space_all = []
        space_names_all = []
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
        new_shape = [(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_min, y_max)]
        dims = ((x_max - x_min), (y_max - y_min))
        space_points = new_shape
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
        self.space_name.append(name)
        self.points.append(points)
        self.lines.append(space_lines)
        self.spaces.append(space_area)
        self.space_all.extend(space_all)
        self.space_names_all.extend(space_names_all)
        self.total_spaces +=1


    def generate_area(self, dict_or_tuple_of_dims, origin_point):
        if isinstance(dict_or_tuple_of_dims, dict):
            dict_of_dims = dict_or_tuple_of_dims
        elif isinstance(dict_or_tuple_of_dims, tuple):
            dict_of_dims = {'name': dict_or_tuple_of_dims}
        else:
            raise ValueError('Input should be a dictionary or a tuple')
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
        self.total_spaces +=1

    def generate_rotated_90(self, dict_or_tuple_of_dims, origin_point):
        if isinstance(dict_or_tuple_of_dims, dict):
            dict_of_dims = dict_or_tuple_of_dims
        elif isinstance(dict_or_tuple_of_dims, tuple):
            dict_of_dims = {'name': dict_or_tuple_of_dims}
        else:
            raise ValueError('Input should be a dictionary or a tuple')
        points = []
        space_all = []
        space_names_all = []
        
        for name, dims in dict_of_dims.items():
            space_center = (origin_point[0] + dims[0]/2, origin_point[1] + dims[1]/2)
            space_corners = [(space_center[0] - dims[1]/2, space_center[1]- dims[0]/2),
                            (space_center[0] + dims[1]/2, space_center[1] - dims[0]/2),
                            (space_center[0] + dims[1]/2, space_center[1] + dims[1]/2),
                            (space_center[0] - dims[1]/2, space_center[1] + dims[1]/2)]
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
        self.total_spaces +=1

    def add_area_e(self, dict_or_tuple_of_dims):
        if isinstance(dict_or_tuple_of_dims, dict):
            dict_of_dims = dict_or_tuple_of_dims
        elif isinstance(dict_or_tuple_of_dims, tuple):
            dict_of_dims = {'a0': dict_or_tuple_of_dims}
        else:
            raise ValueError('Input should be a dictionary or a tuple')
        points = []
        space_all = []
        space_names_all = []
        starting_corner = self.points[self.total_spaces-1][1]
        for name, dims in dict_of_dims.items():
            starting_point = self.points[self.total_spaces -1][1]
            space_center = ((starting_point[0] + dims[0]/2), (starting_point[1] + dims[1])/2) 
            # Define the coordinates of the four corners of the space
            space_corners = [(space_center[0] - dims[0]/2, space_center[1] - dims[1]/2),
                            (space_center[0] + dims[0]/2, space_center[1] - dims[1]/2),
                            (space_center[0] + dims[0]/2, space_center[1] + dims[1]/2),
                            (space_center[0] - dims[0]/2, space_center[1] + dims[1]/2)]
            self.points.append(space_corners)
            # Generate lines connecting the points
            lines_list = []
            for i in range(len(space_corners)):
                line = (space_corners[i], space_corners[(i+1)%len(space_corners)])
                lines_list.append(line)
            self.lines.append(lines_list)
            # Calculate the surface area of the space
            space_surface = dims[0] * dims[1]
            self.spaces.append(space_surface)
            # Add all the space data to the space_all list
            space_all_comp = []
            space_all_comp.append(name)
            space_all_comp.extend(space_corners)
            space_all_comp.extend(lines_list)
            space_all_comp.append(space_surface)
            self.space_all.append(space_all_comp)
            # Add all the space names to the space_names_all list
            names_list = [dims]
            for j in range(len(space_corners)):
                point_name = f"{dims}_p{j}"
                names_list.append(point_name)
            for j in range(len(lines_list)):
                line_name = f"{dims}_l{j}"
                names_list.append(line_name)
            surface_name = f"{dims}_s0"
            names_list.append(surface_name)
            self.space_names_all.append(names_list)
            self.total_spaces +=1
    
    #### NEEDS RTEFACTORING AND UPDATING
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

#### NEEDS RTEFACTORING AND UPDATING
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

#### NEEDS RTEFACTORING AND UPDATING
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

