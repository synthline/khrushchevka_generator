def generate_layouts():
    areas = {
        'A': [(0, 0), (2600, 0), (0, 5600), (2600, 5600)],
        'C': [(5800, 0), (8400, 0), (5800, 5600), (8400, 5600)]
    }
    
    lines = {
        'line_1': 2600,
        'line_2': 2600,
        'line_3': 2600,
        'line_4': 2600,
        'line_5': 3200,
        'line_6': 3200,
        'line_7': 3200,
        'line_8': 3200
    }
    
    line_positions = {
        1200: [1200, 4400],
        1600: [1600, 4000],
        2400: [2400, 3200],
        3200: [3200, 2400]
    }

    layouts = []

    for line_name, line_length in lines.items():
        for area_name, area_coords in areas.items():
            for position, (top, bottom) in line_positions.items():
                if line_length == 2600 and position in (1200, 2400, 1600, 3200):
                    top_layout = (area_name, line_name, top)
                    bottom_layout = (area_name, line_name, bottom)
                    layouts.append(top_layout)
                    layouts.append(bottom_layout)
                elif line_length == 3200 and position in (1200, 2400, 1600, 3200):
                    top_layout = (area_name, line_name, top)
                    bottom_layout = (area_name, line_name, bottom)
                    layouts.append(top_layout)
                    layouts.append(bottom_layout)

    return layouts

possible_layouts = generate_layouts()
for layout in possible_layouts:
    print(layout)

