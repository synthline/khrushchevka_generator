import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Define the area dimensions and origin point
origin_points = [(1.0, 1.0)]
areas_dims = [{'area_0': (26, 56)}, {'area_1': (32, 56)}]

### Generated ###
areas_surfaces = []
areas_points = []
areas_lines = []

def generate_surface_area(list_of_dims):
    for area in list_of_dims:
        for key, value in area.items():
            area_surface = value[0] * value[1]
            areas_surfaces.append(area_surface)

def generate_points(list_of_dims, origin_point):
    for i, items in enumerate(list_of_dims):
        for key, value in items.items():
            # Calculate the coordinates of the space
            space = key
            space_center = (origin_point[0] + value[0]/2, origin_point[1] + value[1]/2)
            # Define the coordinates of the four corners of the space
            space_corners = [(space_center[0] - value[0]/2, space_center[1] - value[1]/2),
                             (space_center[0] + value[0]/2, space_center[1] - value[1]/2),
                             (space_center[0] + value[0]/2, space_center[1] + value[1]/2),
                             (space_center[0] - value[0]/2, space_center[1] + value[1]/2)]
            # Append the first point to the end of the list to close the polygon
            space_corners.append(space_corners[0])
            areas_points.append(space_corners)
            if i == 0:
                origin_points.append(space_corners[1])
            origin_point = space_corners[0]
    return areas_points



# Generate the points for the areas
generate_points(areas_dims, origin_points[0])

print(origin_points)
