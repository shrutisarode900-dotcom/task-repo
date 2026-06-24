# Read attendance data from file
f = open("attendance.txt", "r")

print("Attendance Records: ")
print(f.read())
f.close()