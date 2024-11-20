
decimalNumber = int(input("enter a number from 0 to 15: "))
if decimalNumber < 0 or decimalNumber > 15: 
    print("number is out of range")
else:
    hexvalue = hex(decimalNumber)
    print(hexvalue [2:])

