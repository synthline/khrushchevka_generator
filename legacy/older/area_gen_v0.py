m_len_1 = 2600
m_len_2 = 3200
max_len = (2 * m_len_1) + m_len_2
width = 5600

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
    
    for key, value in my_dict.items():
        print(key + '-' + str(value[0]) + 'x' + str(value[1]))

create_dict(m_len_1, m_len_2, htk, room)

