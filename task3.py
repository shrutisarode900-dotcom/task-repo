# Bus Seat cheaker
n=int(input("Enetr number of seat chekers: "))
available = 0
unavailable = 0
for i in range(n):
    seat=input("Enetr the seat's(available/unavailable):")
    if seat == "available":
        available = available+1
    elif seat == "unavailable":
        unavailable = unavailable+1
print("total available seats : ",available)
print("unavilable seats: ", unavailable)        
