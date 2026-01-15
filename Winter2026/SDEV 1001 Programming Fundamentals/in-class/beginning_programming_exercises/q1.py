#1. Ask the user for a temperature in Celsius and convert it to Fahrenheit.
celsius = input("Temperature in *C: ")
CELSIUS_TO_FAHRENHEIT = (float(celsius) * (9/5) + 32)
print(F"Celsius: {celsius} => Fahrenheit: {CELSIUS_TO_FAHRENHEIT}")