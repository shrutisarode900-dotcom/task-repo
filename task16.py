# file handling
name = input("Enter customer name: ")
f = open("customer.txt","w")
f.write(name)
f.close()

f=open("customer.txt","r")
print("customer name:",f.read())
f.close()