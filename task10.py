# Delivey charge
def delivery_charge(order_amount):
    if order_amount >= 500:
        return 0
    else:
        return 50
amount = float(input("enter order amount: "))
charge=  delivery_charge(amount)

print("delivery charge:", charge)