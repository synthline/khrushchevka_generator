import matplotlib.pyplot as plt

# Define the maximum size of the graph
max_graph_size = (2, 4)

# Define the coordinates of the triangle as tuples of (x, y)
shape_coords = [(1, 1), (2, 4), (3, 1)]

# Add the first point to the end of the list to close the triangle
shape_coords.append(shape_coords[0])

# Extract the x and y coordinates from the tuples
x, y = zip(*shape_coords)

# Create a new plot
fig, ax = plt.subplots()

# Plot the triangle
ax.plot(x, y, color='blue')

# Get the current axis limits
xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()

# Find the minimum and maximum x and y values for the triangle
min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)

# Set the new axis limits to include the entire triangle plus a margin of (2, 2)
ax.set_xlim([min_x - max_graph_size[0], max_x + max_graph_size[0] + 2])
ax.set_ylim([min_y - max_graph_size[1], max_y + max_graph_size[1] + 2])

# Create a dictionary of the points, lines, and shape
shape_dict = {
    'point1': shape_coords[0],
    'point2': shape_coords[1],
    'point3': shape_coords[2],
    'line1': (shape_coords[0], shape_coords[1]),
    'line2': (shape_coords[1], shape_coords[2]),
    'line3': (shape_coords[2], shape_coords[0]),
    'shape': tuple(shape_coords)
}

# Display the dictionary
print(shape_dict)
# Output: {'point1': (1, 1), 'point2': (2, 4), 'point3': (3, 1), 'line1': ((1, 1), (2, 4)), 'line2': ((2, 4), (3, 1)), 'line3': ((3, 1), (1, 1)), 'triangle': ((1, 1), (2, 4), (3, 1), (1, 1))}

# Display the plot
plt.show()
