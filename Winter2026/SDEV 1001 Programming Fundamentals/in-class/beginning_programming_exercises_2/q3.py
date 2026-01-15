# A bag of cookies holds 40 cookies. The calorie information on the bag claims that there are 10 "servings" in the bag and that a serving equals 300 calories. Write a program that asks the user to input how many cookies they ate and then reports how many total calories were consumed.

#get user's amount of cookies eaten
user_cookies_eaten = float(input("How many cookies did you eat? "))

#calculate how many calories were consumed 
#**calorie information on the bag claims 10 "servings" is equal to 300calories**
#a bag holds 40 cookies
cookies_in_a_bag = 40
servings_per_bag = 10
calories_per_serving = 300

cookies_per_servings = (cookies_in_a_bag/servings_per_bag)

calories_consumed = user_cookies_eaten / cookies_per_servings * calories_per_serving
#display how many cookies it is
print(f"You ate {user_cookies_eaten} cookies")

#display how many caloies were consumed
print(f"Which is equal to: {calories_consumed:.1f} calories")