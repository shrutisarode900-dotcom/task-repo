# function
# salary calculator
def calculate_salary(salary,bonus):
    final_salary= salary + bonus
    return final_salary
salary = int(input("enter the salary : "))
bonus = int(input("enter the bonus: "))
total = calculate_salary(salary,bonus)

print("total salary :", total)
