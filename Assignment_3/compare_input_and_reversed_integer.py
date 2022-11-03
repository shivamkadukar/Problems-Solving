from utils.input_utils import get_input_number
from reverse_a_number import reverse_integer

def compare_numbers(reversed_integer, input_integer):
    if int(reversed_integer) > int(input_integer):
        print(f"{reversed_integer} is greater than {input_integer}")
    elif int(reversed_integer) < int(input_integer):
        print(f"{reversed_integer} is smaller than {input_integer}")
    else:
        print(f"{reversed_integer} is equal to {input_integer}")

if __name__ == '__main__':
    input_integer = get_input_number(digit_limit=5)
    reversed_integer = reverse_integer(input_integer)
    compare_numbers(reversed_integer, input_integer)