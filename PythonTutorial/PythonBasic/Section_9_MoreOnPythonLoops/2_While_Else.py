# in this tutorial, you’ll learn about the Python while else statement and how to use it effectively.
# in python, the condition is checked at the beginning of each iteration, the code block inside the while statement will execute as long as the condition is true
# when the condition becomes false and the loop runs normally, the else clause will execute
# if the loop is terminated permaturely by either a break or return statement, the else clause won't execute.
# suppose that we have a list of fruits where each fruit is a dictionary that consists of the fruit name and qty keys:
# we want to make a program that allows the users to enter a fruit name, based on the input name, we'll search for is from the list and show its quantity if the fruit is on the list
basket = [
    {'fruit': 'apple', 'qty': 20},
    {'fruit': 'banana', 'qty': 30},
    {'fruit': 'orange', 'qty': 10}
]

fruit = input("Enter a fruit: ").lower()
index = 0
test_found = False

while index < len(basket):
    item = basket[index]
    if item['fruit'] == fruit:
        test_found = True
        print(f"the bascket has {item['qty']} {item['fruit']}(s))")
        break
    
    index += 1
        
else:
    
    qty = int(input(f"enter the qty of the {fruit}: "))
    basket.append({'fruit': fruit, 'qty': qty})
    print(basket)