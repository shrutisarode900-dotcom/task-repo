def calculate_ratio():
    try:
        amount=float(input("Enter number of amounts:"))
        accounts = int(input("enter number of accounts: "))

        ratio = amount / accounts

        print("ratio = ", ratio)
    except ZeroDivisionError:
        print("number of accounts cannot be zero")   
    except ValueError:
        print("please enter valid nummeric values")     

calculate_ratio()    