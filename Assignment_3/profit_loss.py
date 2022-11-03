def calculate_profit_loss(cost_price, selling_price):
    difference = selling_price - cost_price
    if difference > 0:
        print(f'PROFIT = {abs(difference)}')
    elif difference < 0:
        print(f'LOSS = {abs(difference)}')
    else:
        print('selling price is same as cost price')


if __name__ == '__main__':
    cost_price = int(input(f'Enter cost price: '))
    selling_price = int(input(f'Enter selling price: '))

    calculate_profit_loss(cost_price, selling_price)