
import math 

year = int(input("Enter year: "))
m = month = int(input("Enter month: "))
j = year // 100 #столетие 
k = year % 100 # год столетия 

if m == 1:
    m = 13 # коректируем месяц
    year -= 1 # переход на предыдущий год
elif m == 2:
    m = 14
    year -= 1



if month in [1, 3, 5, 7, 8, 10, 12]:
    print("You can enter the day of a month (1-31)")
    q = days = int(input("Enter the day of a month (1-31): "))
elif month in [4, 6, 9, 11]:
    print("You can enter the day of a month (1-30)")
    q= days = int(input("Enter the day of a month (1-30): "))
elif year % 4 == 0 and month == 2: 
    print("You can enter the day of a month (1-29)")
    q = days = int(input("Enter the day of a month (1-29): "))
else:
    print("You can enter the day of a month (1-28)")
    q = days = int(input("Enter the day of a month (1-28): "))



h = (q + math.floor((26*(m+1)/10)) + k + math.floor(k/4) + math.floor(j/4) + 5*j) % 7 # получаем число дня недели

daysOfWeek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] # названия дней недели

print ("The day of the week is", daysOfWeek[h]) # присваиваем названию дня недели число и выводим его из списка 

    
