#Ask for the price of an item and the quantity purchased. Display the amount of the total including GST.

price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
GST_RATE = .05

total_GST = price * quantity * GST_RATE

total_price = total_GST + (price *quantity)

print(f"Purchasing {quantity} of this item worth ${price:.2f} including the GST amount of ${total_GST:.2f} is ${total_price:.2f}")