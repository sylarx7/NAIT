#Ask the user for a number of miles and print out how many kilometres it is. Display to 2 decimal places.
#The conversion rate is 1 mile = 1.609344 kilometers

miles = float(input("Enter the number of miles: "))
miles_to_km_conversion_rate = 1.609344

result = miles * miles_to_km_conversion_rate

print(f"{miles:.1f} miles is {result:.2f} kilometers. ")