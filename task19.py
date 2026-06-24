# count words in a report file 

f = open("report.txt","r")

text = f.read()
words = len(text.split())

print("total words: ",words)

f.close()