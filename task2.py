# ATM transaction counter 
n=int(input("Enter number of transactions: "))
deposit=0
withdrawal =0
for i in range (n):
    transaction = input ("enter transaction (deposit/withdrawal): ")

    if transaction == "deposit":
        deposit = deposit+1
    elif transaction == "withdrawal":
        withdrawal = withdrawal+1

print("total deposits =",deposit)
print("total withdrawals =", withdrawal)
