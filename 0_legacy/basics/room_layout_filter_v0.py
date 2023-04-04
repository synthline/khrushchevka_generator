import itertools

def read_file(filename):
    with open(filename, 'r') as file:
        # Read each line and remove any leading/trailing white space characters
        lines = [line.strip() for line in file]
        # Use eval() to convert each line to a tuple of tuples
        tuples = [eval(line) for line in lines]
        return tuples
    
def filter_tuples_all(input_list):
    def check_valid(sub_tuple1, sub_tuple2):
        allowed_chars = set('abcd')
        sub_tuple1_chars = set(sub_tuple1)
        sub_tuple2_chars = set(sub_tuple2)

        # If 'a', 'b', or 'd' appears in one sub-tuple, it is not allowed to appear in the other sub-tuple.
        if ('a' in sub_tuple1_chars and 'a' in sub_tuple2_chars) or \
           ('b' in sub_tuple1_chars and 'b' in sub_tuple2_chars) or \
           ('d' in sub_tuple1_chars and 'd' in sub_tuple2_chars):
            return False

        # 'a', 'b', 'c' and 'd' must appear in the tuple.
        if not (allowed_chars.issubset(sub_tuple1_chars | sub_tuple2_chars)):
            return False

        # 'a', 'b', and 'd' must appear only once in the combined sub-tuples.
        combined_chars = sub_tuple1 + sub_tuple2
        if combined_chars.count('a') != 1 or combined_chars.count('b') != 1 or combined_chars.count('d') != 1:
            return False

        return True

    filtered_list = [t for t in input_list if check_valid(t[0], t[1])]
    return filtered_list

def filter_tuples_abc(input_list):
    def check_valid(sub_tuple1, sub_tuple2):
        allowed_chars = set('abc')
        forbidden_char = 'd'
        sub_tuple1_chars = set(sub_tuple1)
        sub_tuple2_chars = set(sub_tuple2)

        # If 'a' or 'b' appear in one sub-tuple, it is not allowed to appear in the other sub-tuple.
        if ('a' in sub_tuple1_chars and 'a' in sub_tuple2_chars) or \
        ('b' in sub_tuple1_chars and 'b' in sub_tuple2_chars):
            return False

        # 'a', 'b' and 'c' must appear in the tuple.
        if not (allowed_chars.issubset(sub_tuple1_chars | sub_tuple2_chars)):
            return False

        # 'a', 'b' must appear only once in the combined sub-tuples.
        combined_chars = sub_tuple1 + sub_tuple2
        if combined_chars.count('a') != 1 or combined_chars.count('b') != 1:
            return False

        # 'd' must not appear in the combined sub-tuples.
        if forbidden_char in combined_chars:
            return False

        return True

    filtered_list = [t for t in input_list if check_valid(t[0], t[1])]
    return filtered_list


def corner_d_tuples(tuple_input):
    result = []
    for sub_tuple in tuple_input:
        if 'd' in sub_tuple[0][0] or 'd' in sub_tuple[0][3] or 'd' in sub_tuple[1][0] or 'd' in sub_tuple[1][3]:
            result.append(sub_tuple)
    return tuple(result)

def corner__bottom_right_d_tuples(tuple_input):
    result = []
    for sub_tuple in tuple_input:
        if 'd' in sub_tuple[1][3]:
            result.append(sub_tuple)
    return tuple(result)


input_list = read_file('0_legacy/basics/results.txt') 
# check if input_list is being populated correctly
#print(input_list)
#print(len(input_list))

abc_tuples = filter_tuples_abc(input_list)
print(abc_tuples)
print(len(abc_tuples))


filtered_tuples = filter_tuples_all(input_list)
d_cornered = corner_d_tuples(filtered_tuples)
#print(d_cornered)
# print(len(d_cornered))

b_right_d_corner = corner__bottom_right_d_tuples(d_cornered)
print(b_right_d_corner)
print(len(b_right_d_corner))


