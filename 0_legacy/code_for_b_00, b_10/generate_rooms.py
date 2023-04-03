room_type_names = ['toilet', 'bathroom', 'kitchen', 'living_room', 'bedroom_1', 'bedroom_2', 'bedroom_3', 'hallway']
room_type_sizes = [(1300, 2600), (2600, 2600), (3900, 2600), (1600, 2600), (4200, 2600), (4500, 2600), (4800, 2600), 
                   (1300, 3200), (2600, 3200), (3900, 3200), (1600, 3200), (4200, 3200), (4500, 3200), (4800, 3200)]

rooms_and_sizes = []

for item1 in room_type_names:
    for item2 in room_type_sizes:
        result_dict = {item1: item2}
        rooms_and_sizes.append(result_dict)

print(len(rooms_and_sizes))
#print(rooms_and_sizes)


