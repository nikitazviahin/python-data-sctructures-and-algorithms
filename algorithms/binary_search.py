from time_it import time_it


@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1
        
        else:
            right_index = mid_index -1

    return -1


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)
        

if __name__ == "__main__":
    # numbers_list = [12,5,6,11,4,567,123,45]
    # number_to_find = 12

    numbers_list = [i for i in range(10000001)]
    number_to_find = 123123

    index_lin = linear_search(numbers_list, number_to_find) #~450 miliseconds
    index_bin = binary_search(numbers_list, number_to_find) #0.01 milisecond
    index_bin_rec = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list)) 
    print(f"Number found at {index_lin} using linear search")
    print(f"Number found at {index_bin} using binary search")
    print(f"Number found at {index_bin_rec} using binary search")