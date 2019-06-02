def smallest(input_list):
    smallest_num = 0
    for element in input_list:
        if element < smallest_num:
            smallest_num = element

    return smallest_num

def largest(input_list):
    largest_num = 0
    for element in input_list:
        if element > largest_num:
            largest_num = element

    return largest_num