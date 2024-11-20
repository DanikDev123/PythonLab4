while True:
    outTemperature = float(input("Enter fahrenheit temperature from -58 to 41 "))
    if -58 <= outTemperature <= 41:
        break
    print("Temperature must be in interval from -58 to 41")

while True:
    windspeed = float(input("Enter wind speed in miles per hour not less than 2 mph "))
    if windspeed >= 2:
        break
    print("Wind speed must be more than 2 mph")

windchill = 35.74 + 0.6215 * outTemperature - 35.75 * (windspeed ** 0.16) + 0.4275 * outTemperature * (windspeed ** 0.16)
print("Wind chill temperature = {windchill:.2f}")
