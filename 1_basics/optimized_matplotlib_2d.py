import matplotlib.pyplot as plt

# Define the maximum size of the graph
max_graph_size = (2, 4)

# Define the coordinates of the triangle as tuples of (x, y)
triangle_coords = [(1, 1), (2, 4), (3, 4), (4,6), (5,7)]

# Add the first point to the end of the list to close the triangle
triangle_coords.append(triangle_coords[0])

# Extract the x and y coordinates from the tuples
x, y = zip(*triangle_coords)

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

# Display the plot
plt.show()