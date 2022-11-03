from utils.input_utils import get_input_number, get_input_list

if __name__ == '__main__':
    print('Enter size of input list')
    N = get_input_number()

    L1 = get_input_list(N)

    print('Enter number to mulitply with the list elements')
    M = get_input_number()

    L2 = [i * M for i in L1]

    print(f'L1 = {L1}, L2 = {L2}')