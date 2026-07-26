def main():
    total_amount = 0
    coke_price = 50

    while total_amount < coke_price:
        inserted_amount = int(input('Insert a coin: '))
        if inserted_amount == 25 or inserted_amount == 10 or inserted_amount == 5:
            total_amount += inserted_amount
            print(calc(total_amount, coke_price))

def calc(total, product_price):
    current_amount = product_price - total
    if 0 < current_amount < product_price:
        return f'Amount Due: {current_amount}'
    if current_amount <= 0:
        return f"Change Owed: {current_amount * -1}"

main()