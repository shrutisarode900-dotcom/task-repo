# Student grade cheaker
def check_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "Fail"
marks= int(input("Enter the marks : "))
grade= check_grade(marks) 
print("Grade: ",grade)   