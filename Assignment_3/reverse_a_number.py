from utils.input_utils import get_input_number

def reverse_integer(input_integer):
    
    reversed_integer = str(input_integer)[::-1]
    return reversed_integer
    

if __name__ == '__main__':
    input_integer = get_input_number(digit_limit=5)
    reversed_integer = reverse_integer(input_integer)
    print(f"The reversed number is: {reversed_integer}")