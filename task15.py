# Age verification
def verify_age():
    try:
        age =int(input("Enter the age:  "))
        if age >=18:
            print("eligible for voting !!")

        else:
            print("not eligible for voting")
    except ValueError:
        print("please enter the valid age...") 
verify_age()                   
