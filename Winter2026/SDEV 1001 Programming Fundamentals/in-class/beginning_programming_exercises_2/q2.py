# Write a program that asks the user to enter three test scores. The program should display each test score, as well as the average test of the users' scores.

#ask for first test score
user_first_test_score = float(input("Enter the first test score: "))

#ask for second test score
user_second_test_score = float(input("Enter the second test score: "))

#ask for third test score
user_third_test_score = float(input("Enter the third test score: "))

#get average
average_score = (user_first_test_score + user_second_test_score + user_third_test_score) / 3

#display each test scores then display average. display with 1 decimal place.
print(f"Test Score 1: {user_first_test_score:.1f}")
print(f"Test Score 2: {user_second_test_score:.1f}")
print(f"Test Score 3: {user_third_test_score:.1f}")

print(f"Average Score: {average_score:.1f}")