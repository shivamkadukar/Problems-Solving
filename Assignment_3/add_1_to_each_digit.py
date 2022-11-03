from utils.input_utils import get_input_number

if __name__ == '__main__':
    print('Enter a number(max 5 digits): ')
    N = get_input_number(digit_limit=5, exact_digits= True)

    new_number = ''
    for i in str(N):
        new_number += str(int(i) + 1)

    print(f'M = {new_number}')
        
