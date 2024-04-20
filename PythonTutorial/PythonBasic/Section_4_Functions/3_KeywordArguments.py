# in this tutorial, you’ll learn about the Python keyword arguments, and how to use them to make function calls more obvious.

# suppose you define a function like: def funtion(parameter1,parameter2):
# when you call it, you input "function(value1,value2)", actually you pasa each argument as a position argument,
# in the other word, you pass the value1 to parameter1 first and the value2 parameter2 second

# however, the function call "functio(value1,value2)" has a readability issue, by looking at it only, you don't know which argument is paramter1 and which one is parameter2
# to improve the readability, python introduces the keyword arguments

#the basical syntax of keyword arguments is as follows:
#fn(parameter1 = value1,parameter2 = value2)

# for example:
def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

net_price = get_net_price(price=100, discount=0.06)
print(net_price)

# it should be noted that once you use the keyword arguments, you need to use keyword arguments for the remaining parameters.
# an example of a mistake: fn(value1,parameter2 = value2,value3)