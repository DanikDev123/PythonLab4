a, b, c, d, e, f = map(float,input("Enter a, b, c, d, e, f: ").split(','))
# 9, 4,3,-5,-6,-21



x = (e*d - b*f) / (a*d - b*c)
y = (a*e - c*d) / (a*f - b*d)

if a*d - b*c == 0:
    print("The equation has no solution")
    
else:
    print("x = ", x)
    print("y = ", y)
    
