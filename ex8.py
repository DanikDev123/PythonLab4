

outTemperature = float(input("Enter fahrenheit temperature not less than to 41 "))
windspeed = float(input("Enter wind speed in miles per hour not less than 2 mph "))

if outTemperature < 41 or windspeed < 2:
    if outTemperature < 41:
        print("Temperature must be more than 41 degrees")
    if windspeed <= 2:
        print("Wind speed must be more than 2 mph")
else: 

    windchill = 35.74 + 0.6215 * outTemperature - 35.75 * (windspeed ** 0.16) + 0.4275 * outTemperature * (windspeed ** 0.16)
    print("Wind chill temperature = ", windchill)