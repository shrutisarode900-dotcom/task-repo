# file report reader
def read_report():
    try:
        file = open ("report.txt","r")
        content = file.read()
        print(content)
        file.close()

    except FileNotFoundError:
        print("report file not found ") 
read_report()           