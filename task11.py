def online_payment():
    try:
        amount = float(input("enter the payment amount: "))
        if amount <= 0:
            print("invalid payment amount!")
        else:
            print("payment of ",amount,"Payment Successfully.")

    except ValueError:
        print("please enter a valid numeric amount.")
online_payment()        