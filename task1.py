a=int(input("Enter the number of days: "))
b=int(input("enter the sale amount for each day: "))
total = 0

for i in range (a):
    sale = float(input("enter sale: "))
    total = total + sale
print("total sale: ",total)    
