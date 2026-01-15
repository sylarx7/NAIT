# Ask the user for a currency amount and display the number of dollars, quarters, dimes, nickels, and pennies in that amount. Display appropriate inputs and outputs

#ask user for a currency amount
user_currency_amount = float(input("Currency Amount: "))

#Calculate how many of the following 
#in dollars
number_of_dollars = int(user_currency_amount)

remaining_amount = float(user_currency_amount - number_of_dollars)

#in quarters
number_of_quarters =  int(remaining_amount / .25)
remaining_amount = remaining_amount % .25

#in dimes
number_of_dimes = int(remaining_amount / 0.1)
remaining_amount = remaining_amount % 0.1

#in nickels
number_of_nickels = int(remaining_amount / 0.05)

#in pennies
remaining_amount = remaining_amount % 0.05
number_of_pennies = int(round(remaining_amount / 0.01))

#display result
print(f"Number of Dollars: {number_of_dollars}")
print(f"Number of Quarters: {number_of_quarters}")
print(f"Number of Dimes: {number_of_dimes}")
print(f"Number of Nickels: {number_of_nickels}")
print(f"Number of Pennies: {number_of_pennies}")