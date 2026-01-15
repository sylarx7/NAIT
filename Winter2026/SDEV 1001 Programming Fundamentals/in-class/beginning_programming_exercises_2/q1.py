# One acre of land is equal to 43,560 square feet. Write a program that asks the user to enter the total square feet in a tract of land and calculates the number of acres in the tract.

#ask user for how many acres
user_acres = float(input("Acre to Square foot converter. How many acres do you have? "))
#convert the acres to square feet
ACRE_TO_SQUARE = user_acres * 43560

#display result
print(f"You have {user_acres} which is equal to {ACRE_TO_SQUARE} square feet")