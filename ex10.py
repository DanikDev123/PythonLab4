
v1_x, v1_y = (0,0)
v2_x, v2_y = (200,0)
v3_x, v3_y = (0,100)

x1, y1= map(float, input("Enter a point x and y coordinates: ").split(','))

if x1 > v1_x and x1 < v2_x and y1 > v1_y and y1 < v3_y:
    print("The point is in the triangle")
else:
    print("The point is not in the triangle")