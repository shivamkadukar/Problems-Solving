from utils.input_utils import get_input_number, get_input_list

if __name__ == '__main__':

    print('Enter size of input list')
    N = get_input_number()

    L1 = get_input_list(N)

    print('Enter number to check divisibility')
    D = get_input_number()

    L2 = [i for i in L1 if i % D == 0]

    print(f'L1={L1}, N={N}, D={D}, L2={L2}, Size of L2={len(L2)}')