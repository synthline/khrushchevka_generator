import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Define the area dimensions and origin point
areas_dims = [{'area_0': (26, 56)}, {'area_1': (32, 56)}]

def generate_points(list_of_dims, origin_point):
    areas_points = []
    space_points = []
    prev_point = origin_point
    for i, items in enumerate(list_of_dims):
        for key, value in items.items():
            # Calculate the coordinates of the space
            space_center = (prev_point[0] + value[0]/2, prev_point[1] + value[1]/2)
            # Define the coordinates of the four corners of the space
            space_corners = [(space_center[0] - value[0]/2, space_center[1] - value[1]/2),
                             (space_center[0] + value[0]/2, space_center[1] - value[1]/2),
                             (space_center[0] + value[0]/2, space_center[1] + value[1]/2),
                             (space_center[0] - value[0]/2, space_center[1] + value[1]/2)]
            # Append the first point to the end of the list to close the polygon
            space_corners.append(space_corners[0])
            areas_points.append(space_corners)
            space_points.append(space_corners)
            prev_point = space_corners[0]

    # Set the origin point for the second area based on the position of the first area
    origin_point_1 = (space_points[0][1][0] + 1, space_points[0][1][1])
    # Adjust the points of the second area to be adjacent to the first area
    for point in areas_points[len(list_of_dims[0]) + 1:]:
        point[0] += (origin_point_1[0] - space_points[1][0][0], 0)
        point[1] += (origin_point_1[0] - space_points[1][0][0], 0)
        point[2] += (origin_point_1[0] - space_points[1][0][0], 0)
        point[3] += (origin_point_1[0] - space_points[1][0][0], 0)
        space_points.append(point)
    # Make sure the space points are aligned between the two areas
    space_points[1][3] = space_points[0][2]
    return areas_points, origin_point_1


def generate_lines(list_of_points):
    areas_lines = []
    for area_points in list_of_points:
        line_0 = (area_points[0], area_points[1]) 
        line_1 = (area_points[1], area_points[2]) 
        line_2 = (area_points[2], area_points[3]) 
        line_3 = (area_points[3], area_points[0]) 
        areas_lines.append(line_0)
        areas_lines.append(line_1)
        areas_lines.append(line_2)
        areas_lines.append(line_3)
    return areas_lines

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

def plot_all(list_of_points, list_of_lines):
    fig, ax = plt.subplots()
    for i, lines in enumerate(list_of_lines):
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

def main():
    origin_point = (1, 1)
    areas_points, prev_point = generate_points(areas_dims, origin_point)
    areas_lines = generate_lines(areas_points)

    plot_points(areas_points)
    plot_lines(areas_lines)
    plot_areas(areas_points)
    plot_all(areas_points, areas_lines)

if __name__ == '__main__':
    main()

