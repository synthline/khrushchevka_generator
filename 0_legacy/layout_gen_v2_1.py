def generate_layouts():
    areas = {
        'A': [(0, 0), (2600, 0), (0, 5600), (2600, 5600)]
    }
    
    lines = {
        'line_1': 2600   
    }
    
    line_positions = {
        1200_1: [1200, 4400],
        1600_1: [1600, 4000],
        2400_1: [2400, 3200],
        3200: [3200, 2400],
        1200_2: [1200, 2400],
        1600_2: [1600, 3200],
        2400_2: [3200, 2400]
    }

    layouts = []

    for line_name, line_length in lines.items():
        for area_name, area_coords in areas.items():
            for position, (top, bottom) in line_positions.items():
                if line_length == 2600 and position in (1200, 2400, 1600, 3200):
                    top_layout = (area_name, line_name, top)
                    bottom_layout = (area_name, line_name, bottom)
                    new_areas = {
                        area_name + '_top': [(x + top, y) for (x, y) in area_coords],
                        area_name + '_bottom': [(x + bottom, y) for (x, y) in area_coords]
                    }
                    layouts.append((top_layout, new_areas[area_name + '_top']))
                    layouts.append((bottom_layout, new_areas[area_name + '_bottom']))
                elif line_length == 3200 and position in (1200, 2400, 1600, 3200):
                    top_layout = (area_name, line_name, top)
                    bottom_layout = (area_name, line_name, bottom)
                    new_areas = {
                        area_name + '_top': [(x + top, y) for (x, y) in area_coords],
                        area_name + '_bottom': [(x + bottom, y) for (x, y) in area_coords]
                    }
                    layouts.append((top_layout, new_areas[area_name + '_top']))
                    layouts.append((bottom_layout, new_areas[area_name + '_bottom']))

    return layouts

possible_layouts = generate_layouts()
num_combinations = len(possible_layouts)
print(f"Total Number of Possible Combinations: {num_combinations}\n")
for layout, new_area_coords in possible_layouts:
    print('Layout:', layout)
    print('New Areas and Coordinates:')
    for coords in new_area_coords:
        print(coords)
    print('-' * 30)
