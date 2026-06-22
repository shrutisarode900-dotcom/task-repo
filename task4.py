n = int(input("Enter the number of temperature Analyzer: "))
for i in range(n):
    temperature = float(input("Enter the temperature: "))
    if temperature < 0 :
        print("freezing temperature",temperature)
    elif temperature >= 0 :
        print("Normal temperature", temperature) 
    elif temperature > 100:
        print("boiling temperature", temperature) 
    elif temperature >=100:
        print("very hot temperature", temperature)
    else:
        print("invalid temperature",temperature)