from utils.input_utils import get_input_list, get_input_number

def find_max_and_its_position(list):
    max_value = max(list)
    max_position = list.index(max_value)

    return max_value, max_position

def find_min_and_its_position(list):
    min_value = min(list)
    min_position = list.index(min_value)

    return min_value, min_position

if __name__ == '__main__':
    print('Input Size of list')
    size_of_list = get_input_number()
    
    input_list = get_input_list(size_of_list)
    max_value, max_position = find_max_and_its_position(input_list)
    min_value, min_position = find_min_and_its_position(input_list)

    print(f'Largest integer={max_value}, Position of Largest integer={max_position+1},\
            Smallest integer={min_value}, Position of smallest integer={min_position+1}')
