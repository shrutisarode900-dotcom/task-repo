def book_tiket():
    try:
        seat_no =int(input("enter the seat number:" ))
        if seat_no < 1 or seat_no > 100:
            print("invalid seat number")
        else:
            print("seat", seat_no ,"booked successfully!!") 
    except ValueError:
       print("please enter the valid seat number")

book_tiket()

