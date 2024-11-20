import math 
a = int (input("Enter a: "))
b = int (input("Enter b: "))
c = int (input("Enter c: "))

D = b**2 - 4*a*c

r1 = (-b + math.sqrt(D))/2*a
r2 = (-b - math.sqrt(D))/2*a
r3 = -b/2*a

if D > 0:
    print("Root 1: ", r1)
    print("Root 2: ", r2)
elif D == 0:
    print("The root is", r3)
else:
    print("The equation has no real roots")