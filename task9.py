# Shopping discount
def shopping_discount(price,discount):
    discounted_price = price -(price * discount / 100)
    return discounted_price

price=float(input("Enter the price: "))
discount = float(input("enter the discount(%): "))
final_price = shopping_discount(price,discount)
print("discounted  price: ",final_price)
