month = int(input("Enter month: "))
year = int (input("Enter year: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
elif year % 4 == 0 and month == 2: 
    days = 29
else: 
    days = 28
print("There are", days, "days in", month, "month of", year)