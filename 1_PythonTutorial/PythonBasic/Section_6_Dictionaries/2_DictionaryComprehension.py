# in this tutorial, you’ll learn about Python dictionary comprehension to transform or filter items in a dictionary.
# a dictionary comprehension allows you to run a for loop on a dictionary 
# and do something on each item like transforming or filtering and returns a new dictionary
# unlike a for loop, the dictionary comprehension offers a more expressive and concise syntax when you use it correctly
# the basic syntax of the dictionary comprehension is as follows:
# {key:value for (key,value) in dict.items if condition}
# it will return a new dictionary whose item specified by the expression key:value

# now let's take an example:
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}
# suppose that you want to increase the price of each stock by 2%
new_stocks = {name:stock*1.2 for name,stock in stocks.items()}
print(new_stocks)

# and you can use the comprehension to filter a dictionary
# suppose that you want to select stocks whose price are greater than 200
new_stocks = {name:stock for (name,stock) in stocks.items() if stock>200}
print(new_stocks)