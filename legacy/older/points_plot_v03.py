import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Define the area dimensions and origin point
univ_origin = (1, 1)
areas_dims = [{'area_0': (26, 56)}]
#areas_dims = [{'area_0': (26, 56)}, {'area_1': (32, 56)}]
areas_points_coordinates_lines_surfaces = []

def generate_points_coordinates_lines_surfaces(list_of_dims, origin_point):
    # Generate surfaces
    areas_surfaces = []
    for area in list_of_dims:
        for key, value in area.items():
            area_surface = value[0] * value[1]
            areas_surfaces.append(area_surface)

    # Define colors for areas
    colors = ['blue', 'green']

    # Plot the areas
    fig, ax = plt.subplots()
    for i, surfaces in enumerate(areas_surfaces):
        for key, value in list_of_dims[i].items():
            # Calculate the coordinates of the center of the space
            space = key
            space_center = (origin_point[0] + value[0]/2 + i * value[0], origin_point[1] + value[1]/2)
            # Define the coordinates of the four corners of the space
            space_corners = [(space_center[0] - value[0]/2, space_center[1] - value[1]/2),
                             (space_center[0] + value[0]/2, space_center[1] - value[1]/2),
                             (space_center[0] + value[0]/2, space_center[1] + value[1]/2),
                             (space_center[0] - value[0]/2, space_center[1] + value[1]/2)]

            # Define the lines of the space and their point coordinates
            space_lines = [(space_corners[i], space_corners[(i+1)%4]) for i in range(4)]

            # Define the patch and line colors for the space
            space_patch_color = colors[i]
            space_line_color = 'black'

            # Plot the space
            space_patch = plt.Polygon(space_corners, facecolor=space_patch_color, edgecolor=space_line_color)
            ax.add_patch(space_patch)
            for line in space_lines:
                ax.add_line(Line2D(*zip(*line), color=space_line_color))
            plt.xlim(origin_point[0] - value[0]/2 - 1, origin_point[0] + value[0]*len(list_of_dims) + 1)
            plt.ylim(origin_point[1] - value[1]/2 - 1, origin_point[1] + value[1]/2 + 1)

            # Print the coordinates of the space corners, lines, and the space area
            space_area = value[0] * value[1]
            areas_points_coordinates_lines_surfaces.append(space_corners)
            areas_points_coordinates_lines_surfaces.append(space_lines)
            areas_points_coordinates_lines_surfaces.append(space_area)

    plt.show()

generate_points_coordinates_lines_surfaces(areas_dims, univ_origin)
