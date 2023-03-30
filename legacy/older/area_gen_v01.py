import itertools

m_len_1 = 2600
m_len_2 = 3200
max_len = (2 * m_len_1) + m_len_2
max_width = 5600

#hallway, toilet and kitchen
htk = [1200, 1600, 2400]

room = [1600, 2400, 3200, 4000, 5600]

def create_dict(m_len_1, m_len_2, htk, room):
    my_dict = {}
    for i, value in enumerate(htk):
        key_name = f"htk_len1_{i}"
        value_tuple = (m_len_1, value)
        my_dict[key_name] = value_tuple

        key_name = f"htk_len2_{i}"
        value_tuple = (m_len_2, value)
        my_dict[key_name] = value_tuple

    for i, value in enumerate(room):
        key_name = f"room_len1_{i}"
        value_tuple = (m_len_1, value)
        my_dict[key_name] = value_tuple

        key_name = f"room_len2_{i}"
        value_tuple = (m_len_2, value)
        my_dict[key_name] = value_tuple

    combinations = itertools.product([key for key in my_dict.keys() if key.startswith("htk")], 
                                      [key for key in my_dict.keys() if key.startswith("htk")],
                                      [key for key in my_dict.keys() if key.startswith("htk")],
                                      [key for key in my_dict.keys() if key.startswith("room")])

    result = []
    for c in combinations:
        dict_item = {}
        dict_item[c[0]] = my_dict[c[0]]
        dict_item[c[1]] = my_dict[c[1]]
        dict_item[c[2]] = my_dict[c[2]]
        dict_item[c[3]] = my_dict[c[3]]
        result.append(dict_item)

    return result

combinations_list = create_dict(m_len_1, m_len_2, htk, room)
print(f"Total number of unique combinations: {len(combinations_list)}")
print(combinations_list)
