# Append customer feedback to a file
feedback = input("enter feedback: ")
f = open("feedback.txt","a")

f.write(feedback+ "\n")
f.close()

print("feedback saved successfully!!")
