# Count lines in a log file
f = open("log.txt","r")
count = len(f.readlines())
print("total lines: ",count)
f.close()         