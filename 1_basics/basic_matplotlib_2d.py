import matplotlib.pyplot as plt

# Define the coordinates of the triangle
x = [1, 2, 3, 1] # x-coordinates of vertices
y = [1, 3, 1, 1] # y-coordinates of vertices

# Create a new plot
fig, ax = plt.subplots()

# Plot the triangle
ax.plot(x, y, color='blue')

# Set the axis limits
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])

# Display the plot
plt.show()
