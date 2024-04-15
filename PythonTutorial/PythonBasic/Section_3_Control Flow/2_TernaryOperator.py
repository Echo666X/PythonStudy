#in this tutorial, you’ll learn about the Python ternary operator and how to use it to make your code more concise.
#in 3.1,we gave such an example:
# age = input('Enter your age:')

# if int(age) >= 18:
#     ticket_price = 20
# else:
#     ticket_price = 5
# print(f"The ticket price is {ticket_price}")

#However, you can use an alternative syntax to make it more concise
age = int(input("Please enter your age:"))
ticket_price = 20 if age >=18 else 5
print(f"the ticket price is {ticket_price:.2f}")

#the basical syntax of ternary operator as follows:
#value_if_true if condition else value_if_false