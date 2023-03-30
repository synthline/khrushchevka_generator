import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
from itertools import permutations

# Define the origin point
univ_origin = (1, 1)



room_areas = ((3.12, 11.4), (10, 20))



# Define the room dimensions and origin point
univ_origin = (1, 1)
room_1 = (10, 20)
room_name = "Room 1"


def layout_gen(room_areas):

    # Calculate the coordinates of the center of the room
    room_center = (univ_origin[0] + room_1[0]/2, univ_origin[1] + room_1[1]/2)

    # Define the coordinates of the four corners of the room
    room_corners = [(room_center[0] - room_1[0]/2, room_center[1] - room_1[1]/2),
                    (room_center[0] + room_1[0]/2, room_center[1] - room_1[1]/2),
                    (room_center[0] + room_1[0]/2, room_center[1] + room_1[1]/2),
                    (room_center[0] - room_1[0]/2, room_center[1] + room_1[1]/2)]

    # Define the lines of the room and their point coordinates
    room_lines = [(room_corners[i], room_corners[(i+1)%4]) for i in range(4)]

    # Calculate the area of the room
    room_area = room_1[0] * room_1[1]

    # Plot the room
    fig, ax = plt.subplots()
    room_patch = plt.Polygon(room_corners, facecolor='lightblue')
    ax.add_patch(room_patch)
    for line in room_lines:
        ax.add_line(Line2D(*zip(*line)))
    plt.xlim(room_center[0] - room_1[0]/2 - 1, room_center[0] + room_1[0]/2 + 1)
    plt.ylim(room_center[1] - room_1[1]/2 - 1, room_center[1] + room_1[1]/2 + 1)
    ax.set_title(room_name)

    # Add legend with room name and patch color
    plt.legend(handles=[room_patch], labels=[room_name], loc='lower right')

    plt.show()

    # Print the coordinates of the room corners, lines, and the room area
    print("Room corner coordinates:", room_corners)
    print("Room line coordinates:", room_lines)
    print("Room area:", room_area)