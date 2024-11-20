import random 

a = random.randint(0, 100)
b = random.randint(0, 100)
print("a = ", a, "b = ", b)
sum = a + b

answer= int(input("enter sum of two numbers: "))

if sum == answer:
    print("you are right")
else:
    print("you are wrong")