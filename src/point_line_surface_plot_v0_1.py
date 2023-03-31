import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Define the area dimensions and origin point
univ_origin = (1, 1)
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
    point_idx = 0
    for i, items in enumerate(list_of_dims):
        for key, value in items.items():
            # Calculate the coordinates of the space
            space = key
            prev_area_width = 0
            if i > 0:
                prev_area_width = list(list_of_dims[i-1].values())[0][0]
            space_center = (origin_point[0] + prev_area_width + value[0]/2, origin_point[1] + value[1]/2)
            # Define the coordinates of the four corners of the space
            space_corners = [(space_center[0] - value[0]/2, space_center[1] - value[1]/2, f'{space}_p{point_idx}_0'),
                             (space_center[0] + value[0]/2, space_center[1] - value[1]/2, f'{space}_p{point_idx}_1'),
                             (space_center[0] + value[0]/2, space_center[1] + value[1]/2, f'{space}_p{point_idx}_2'),
                             (space_center[0] - value[0]/2, space_center[1] + value[1]/2, f'{space}_p{point_idx}_3')]
            areas_points.append(space_corners)
            point_idx += 1

def generate_lines(list_of_points):
    line_idx = 0
    for i, area_points in enumerate(list_of_points):
        if i > 0:
            prev_area_points = list_of_points[i-1]
            areas_lines.append((prev_area_points[1], area_points[0], f'l{line_idx}'))
            line_idx += 1
        areas_lines.append((area_points[0], area_points[1], f'l{line_idx}'))
        areas_lines.append((area_points[1], area_points[2], f'l{line_idx+1}'))
        areas_lines.append((area_points[2], area_points[3], f'l{line_idx+2}'))
        areas_lines.append((area_points[3], area_points[0], f'l{line_idx+3}'))
        line_idx += 4


# Plot the points
fig, ax = plt.subplots()
for i, points in enumerate(areas_points):
    x, y, names = zip(*points)
    ax.scatter(x, y, label=f'Area {i} Points')
    for j, name in enumerate(names):
        ax.annotate(name, xy=(x[j], y[j]), xytext=(3, 3), textcoords="offset points")
ax.legend()
plt.title('Points')
plt.show()

# Plot the lines
fig, ax = plt.subplots()
for i, line in enumerate(areas_lines):
    x, y, name = zip(*line)
    ax.plot(x, y, label=name)
ax.legend()
plt.title('Lines')
plt.show()

# Plot the area
fig, ax = plt.subplots()
for i, points in enumerate(areas_points):
    x, y, names = zip(*points)
    ax.add_patch(plt.Polygon(points, alpha=0.5, label=f'Area {i}'))
    for j, name in enumerate(names):
        ax.annotate(name, xy=(x[j], y[j]), xytext=(3, 3), textcoords="offset points")
ax.legend()
plt.title('Area')
plt.show()

# Plot the points, lines, and area together
fig, ax = plt.subplots()
for i, lines in enumerate(areas_lines):
    x, y, name = zip(*lines)
    ax.plot(x, y, label=name)
for i, points in enumerate(areas_points):
    x, y, names = zip(*points)
    ax.scatter(x, y, label=f'Area {i} Points')
    for j, name in enumerate(names):
        ax.annotate(name, xy=(x[j], y[j]), xytext=(3, 3), textcoords="offset points")
for i, points in enumerate(areas_points):
    ax.add_patch(plt.Polygon(points, alpha=0.5, label=f'Area {i}'))
ax.legend()
plt.title('Points, Lines, and Area')
plt.show()

   
