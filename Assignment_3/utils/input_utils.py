def get_input_number(digit_limit = None, exact_digits = False):
    input_integer = str(input(': '))

    if digit_limit and exact_digits:
        while len(input_integer) != digit_limit or not input_integer.isdigit():
            print('Input not a number or not equal to digit limits')
            
            input_integer = str(input(': '))
        return int(input_integer)

    elif digit_limit:
        while len(input_integer) > digit_limit or not input_integer.isdigit():
            print('Input not a number or above digit limits')
            
            input_integer = str(input(': '))

        return int(input_integer)

    else:
        while not input_integer.isdigit():
            print(f"Input should be number")

            input_integer = str(input(f': '))
        return int(input_integer)

def get_input_list(size_of_list, element_type = 'integer'):
    output_list = []
    for i in range(0, size_of_list):
        print(f'Enter element {i+1} of list')
        if element_type == 'integer':
            user_input = int(input('Enter a integer number: '))
        elif element_type == 'float':
            user_input = float(input('Enter a decimal number: '))
        else:
            user_input = input('Enter element of list: ')
        output_list.append(user_input)

    return output_list

def get_input_set(cardianality):
    input_set = set()
    for i in range(0, cardianality):
        set_element = input(f'Enter set element {i + 1}: ')
        input_set.update(set_element)

    return input_set



    

