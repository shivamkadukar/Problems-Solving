from utils.input_utils import get_input_list, get_input_number
from find_largest_smallest_number_in_list import find_min_and_its_position

if __name__ == '__main__':
    print('Enter size of input list')
    size_of_list = get_input_number()

    input_list = get_input_list(size_of_list)
    
    print('Enter the number to find smallest in list')
    K = get_input_number()

    i = 1
    duplicate_list = input_list.copy()
    while i <= K:
        min_value, min_value_position = find_min_and_its_position(duplicate_list)

        duplicate_list.pop(min_value_position)
        i += 1

    position = input_list.index(min_value)

    print(f'Kth smallest integer={min_value}, Position of Kth smallest integer={position+1}')