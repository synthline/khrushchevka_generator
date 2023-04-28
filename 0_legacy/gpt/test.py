import math
import itertools
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_combinations(area_A, area_S):
    def generate_new_area(area, direction):
        a, b, c, d = area
        if direction == 'N':
            return (a, (a[0], a[1] + 4000), (d[0], d[1] + 4000), d)
        elif direction == 'E':
            return ((b[0] + 2000, b[1]), (b[0] + 4000, b[1]), (c[0] + 4000, c[1]), b)
        elif direction == 'S':
            return ((a[0], a[1] - 4000), a, d, (d[0], d[1] - 4000))
        elif direction == 'W':
            return ((a[0] - 2000, a[1]), a, (d[0] - 2000, d[1]), (d[0] - 4000, d[1]))

    directions = ['N', 'E', 'S', 'W']
    combinations = []

    for direction in directions:
        combinations.append(generate_new_area(area_S, direction))

    results = []

    for a1, a2 in itertools.product(combinations, repeat=2):
        if not set(a1).intersection(a2) and a1 != a2:
            results.append((a1, a2))

    return results

def plot_areas(combinations):
    fig, ax = plt.subplots(figsize=(15, 15))

    n = len(combinations)
    columns = math.ceil(math.sqrt(n))
    rows = math.ceil(n / columns)
    offset_x = 10000
    offset_y = 10000

    for idx, (a1, a2) in enumerate(combinations, 1):
        row = (idx - 1) // columns
        col = (idx - 1) % columns

        all_areas = [area_A, area_S, a1, a2]
        colors = ['blue', 'red', 'gray', 'gray']

        for i, area in enumerate(all_areas):
            shifted_area = [(x + col * offset_x, y - row * offset_y) for x, y in area]
            polygon = patches.Polygon(shifted_area, edgecolor='k', linewidth=1, facecolor=colors[i], alpha=0.5)
            ax.add_patch(polygon)

            if i == 0:
                ax.text(shifted_area[0][0], shifted_area[0][1] - 1000, f'Combination {idx}', fontsize=10)

    ax.set_xlim(-5000, columns * offset_x)
    ax.set_ylim(-rows * offset_y - 10000, 10000)
    ax.set_aspect('equal', adjustable='box')
    plt.show()

area_A = ((0, 0), (2000, 0), (2000, 4000), (0, 4000))
area_S = ((3000, 3000), (6000, 3000), (6000, 6000), (3000, 6000))
combinations = generate_combinations(area_A, area_S)
plot_areas(combinations)
