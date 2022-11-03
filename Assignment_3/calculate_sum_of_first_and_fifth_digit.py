from utils.input_utils import get_input_number
from utils.calculate_sum_of_digits import calculate_sum_of_digits

if __name__ == '__main__':
    input_integer = get_input_number(digit_limit= 5, exact_digits=True)
    total = calculate_sum_of_digits(input_integer, [1,5])
    print(f"The sum of the digits is: {total}.")