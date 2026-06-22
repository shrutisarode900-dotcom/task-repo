# Electricity bill units
n = int(input("Enter number of customers:"))
threshold =  int(input("Enter the threshold : "))
count=0

for i in range(n):
    units = int(input("enter the units: "))

    if units > threshold:
        count = count+1

print("days crossed threshold=", threshold)