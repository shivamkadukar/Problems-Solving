from utils.input_utils import get_input_number, get_input_set

if __name__ == '__main__':

    print('Enter cardianility of input set A')
    N = get_input_number()
    A = get_input_set(N)

    print('Enter cardianility of input set B')
    M = get_input_number()
    B = get_input_set(M)

    C = A | B
    # same can be achieved by A.union(B)

    D = A & B
    # same can be achieved by A.intersection(B)

    print(f'''set A = {A}, set B = {B}, \n set C = {C}, set D = {D} \n 
            cardianality of set C = {len(C)}, cadianality of set D = {len(D)}''')