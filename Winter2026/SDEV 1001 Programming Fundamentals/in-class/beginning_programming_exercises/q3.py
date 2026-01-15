#Ask the user for the width and height of a rectangle. 
# There could be decimals. Calculate and display the width, height, area, and perimeter
# Calculations print the results rounded to 3 decimal places

user_width = float(input("Rectangle width: "))
user_height = float(input("Rectangle height:"))

rectangle_area = user_width * user_height
rectangle_perimeter = (2 * user_width) + (2 * user_height)

print(user_width)
print(user_height)
print(f"{rectangle_area:.3f}")
print(f"{rectangle_perimeter:.3f}")