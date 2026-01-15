# Ask the user for
# number of pizzas (int)

user_number_of_pizzas = int(input("Number of pizzas: "))

# price per pizza (float, dollars)
user_price_per_pizza = float(input("Price per pizza: $"))

# tip percent (float; e.g., 15 for 15%)
user_tip_percent = float(input("Tips %: ")) / 100

# number of people sharing (int)
user_number_of_people_sharing = int(input("Number of people sharing: "))

# Calculate and print: subtotal, tip amount, total, and amount per person.
subtotal = user_number_of_pizzas * user_price_per_pizza
tip_amount = subtotal * user_tip_percent
total = subtotal + tip_amount
amount_per_person = total / user_number_of_people_sharing

# Formatting currency to 2 decimals. Display appropriate inputs and outputs.
print(f"Number of Pizas ordered: {user_number_of_pizzas}")
print(f"Price per Pizzas: ${user_price_per_pizza:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")
print(f"Amount per person: ${amount_per_person:.2f}")
