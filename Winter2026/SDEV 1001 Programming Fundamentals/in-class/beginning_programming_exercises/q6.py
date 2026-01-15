#Ask the user for the distance they want to travel, the fuel consumption of their vehicle in l/100km and the price per litre. Display the cost for the trip!

user_distance_in_km = float(input("Enter the distance in km: "))

user_fuel_consumption = float(input("Enter the fuel consumption: (liters per 100km): "))

user_price_per_liter = float(input("Enter the price per liter: "))

liter_per_km = float(1/100)
fuel_needed = (user_fuel_consumption * liter_per_km) * user_distance_in_km

total_cost = user_price_per_liter * fuel_needed

print(f"Fuel needed: {fuel_needed} liters")
print(f"Total cost: ${total_cost:.2f}")