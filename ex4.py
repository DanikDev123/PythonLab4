
weight = float(input("Enter weight in pounds: "))
lenghtFeet = float(input("Enter height in feet: "))
lenghtInches = float(input("Enter height in inches: "))

weightKg = weight * 0.453592
heightM = lenghtFeet * 0.3048 + lenghtInches * 0.0254
BMI  = weightKg / heightM ** 2

print("Your BMI is", BMI)

if BMI< 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 25:
    print("Normal weight")
elif BMI > 25 and BMI < 30:
    print("Overweight")
else:
    print("Obese")


