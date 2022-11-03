def calculate_sum_of_digits(input_integer, list_of_digits = []):
    total = 0
    if len(list_of_digits) == 0:      
        for digit in str(input_integer):
            total += int(digit)
    else:
        for digit in list_of_digits:
            total += int(str(input_integer)[digit-1])

    return total