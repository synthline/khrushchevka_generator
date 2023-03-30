import itertools
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_room_layouts(dimensions):
    combinations = list(itertools.product(dimensions, repeat=2))
    layouts = []
    
    for idx, (length, width) in enumerate(combinations):
        layouts.append({
            'index': idx,
            'length': length[0],
            'width': width[1]
        })
    
    return layouts

def visualize_room_layouts(layouts, space_between=5):
    fig, ax = plt.subplots(figsize=(30, 10))
    ax.set_title("All possible room layouts")

    max_width = 0
    for layout in layouts:
        idx, length, width = layout['index'], layout['length'], layout['width']
        x = idx * (space_between + length)
        rect = patches.Rectangle((x, 0), length, width, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)
        ax.text(x + length/2, width/2, f'{length} x {width}', fontsize=12, ha='center', va='center')
        max_width = max(max_width, width)

    ax.set_xlim(0, (space_between + layouts[-1]['length']) * len(layouts))
    ax.set_ylim(0, max_width * 1.1)
    ax.set_aspect('equal')
    plt.show()

room_dimensions = [(10, 10), (12, 12), (15, 10), (20, 20), (10, 15)]
layouts = generate_room_layouts(room_dimensions)
visualize_room_layouts(layouts, space_between=5)
