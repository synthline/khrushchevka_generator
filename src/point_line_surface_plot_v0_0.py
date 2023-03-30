import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Define the area dimensions and origin point
univ_origin = (1, 1)
areas_dims = [{'area_0': (26, 56)}]

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
    return areas_points


def generate_lines(list_of_points):
    for area_points in list_of_points:
        line_0 = (area_points[0], area_points[1]) 
        line_1 = (area_points[1], area_points[2]) 
        line_2 = (area_points[2], area_points[3]) 
        line_3 = (area_points[3], area_points[0]) 
        areas_lines.append(line_0)
        areas_lines.append(line_1)
        areas_lines.append(line_2)
        areas_lines.append(line_3)

def plot_points(list_of_points):
    fig, ax = plt.subplots()
    for i, points in enumerate(list_of_points):
        x, y = zip(*points)
        ax.scatter(x, y, label=f'Area {i} Points')
    #ax.legend()
    plt.title('Points')
    plt.show()
    return list_of_points

def plot_lines(list_of_lines):
    fig, ax = plt.subplots()
    for i, lines in enumerate(list_of_lines):
        x, y = zip(*lines)
        ax.plot(x, y, label=f'Area {i} Lines')
    #ax.legend()
    plt.title('Lines')
    plt.show()

def plot_areas(list_of_points):
    fig, ax = plt.subplots()
    for i, points in enumerate(list_of_points):
        x, y = zip(*points)
        ax.plot(x, y, alpha=0.5, label=f'Area {i}')
    #ax.legend()
    plt.title('Area')
    plt.show()

def plot_all(list_of_points):
    fig, ax = plt.subplots()
    for i, lines in enumerate(areas_lines):
        x, y = zip(*lines)
        ax.plot(x, y, label=f'Area {i} Lines')
    for i, points in enumerate(list_of_points):
        x, y = zip(*points)
        ax.scatter(x, y, label=f'Area {i} Points')
    for i, points in enumerate(list_of_points):
        ax.add_patch(plt.Polygon(points, alpha=0.5, label=f'Area {i}'))
    #ax.legend()
    plt.title('Points, Lines, and Area')
    plt.show()

generate_surface_area(areas_dims)
areas_points = generate_points(areas_dims, univ_origin)
generate_lines(areas_points)

plot_points(areas_points)
plot_lines(areas_lines)
plot_areas(areas_points)
plot_all(areas_points)
