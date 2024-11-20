
number = int(input("enter a number: "))

if number % 5 == 0 and number % 6 == 0:
    divisibleBothNumber = True
else:
    divisibleBothNumber = False
print(f"devisible {number} by 5 and 6 {divisibleBothNumber}")

if number % 5 == 0 or number % 6 == 0:
    divisibleOne = True
else:
    divisibleOne = False
print(f"devisible {number}  by 5 or 6 {divisibleOne}")

if (number % 5 == 0) != (number % 6 == 0):
    divisibleNotBoth = True
else:
    divisibleNotBoth = False
print(f"devisible {number} by 5 or 6, but not both {divisibleNotBoth}")
