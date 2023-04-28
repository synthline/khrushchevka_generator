import matplotlib.pyplot as plt
import matplotlib.patches as patches
from itertools import product

def generate_layouts():
    A = (6400, 6400)
    B = (8000, 4000)
    S = (3200, 6400)

    min_length = 700

    layouts = []

    def adjacent(layout1, layout2):
        horizontal = layout1[2] == layout2[0] and layout1[1] < layout2[3] and layout1[3] > layout2[1]
        vertical = layout1[3] == layout2[1] and layout1[0] < layout2[2] and layout1[2] > layout2[0]
        return horizontal or vertical

    for ax, ay, bx, by in product(range(0, S[0] - min_length + 1, min_length), range(0, S[1] - min_length + 1, min_length), range(0, S[0] - min_length + 1, min_length), range(0, S[1] - min_length + 1, min_length)):
        # Apartment A
        a_left = ax + S[0]
        a_bottom = ay
        a_right = a_left + A[0]
        a_top = a_bottom + A[1]

        # Apartment B
        b_left = bx
        b_bottom = by + S[1]
        b_right = b_left + B[0]
        b_top = b_bottom + B[1]

        # Check if the apartments are adjacent to the staircase
        if not (adjacent((a_left, a_bottom, a_right, a_top), (0, 0, S[0], S[1])) and adjacent((b_left, b_bottom, b_right, b_top), (0, 0, S[0], S[1]))):
            continue

        layouts.append(((a_left, a_bottom, a_right, a_top), (b_left, b_bottom, b_right, b_top)))

    # Display the layouts in a single plot
    plt.figure(figsize=(18, 10))

    for i, layout in enumerate(layouts, start=1):
        ax = plt.subplot(1, len(layouts), i)

        # Draw staircase
        staircase = patches.Rectangle((0, 0), S[0], S[1], linewidth=1, edgecolor='blue', facecolor='none', label='Staircase')
        ax.add_patch(staircase)

        # Draw apartment A
        a = patches.Rectangle((layout[0][0], layout[0][1]), A[0], A[1], linewidth=1, edgecolor='red', facecolor='none', label='Apartment A')
        ax.add_patch(a)

        # Draw apartment B
        b = patches.Rectangle((layout[1][0], layout[1][1]), B[0], B[1], linewidth=1, edgecolor='green', facecolor='none', label='Apartment B')
        ax.add_patch(b)

        ax.set_xlim(-1000, max(A[0], B[0]) + S[0] + 1000)
        ax.set_ylim(-1000, max(A[1], B[1]) + S[1] + 1000)
        ax.legend()
        ax.set_title(f'Layout {i}')

    plt.show()

generate_layouts()
