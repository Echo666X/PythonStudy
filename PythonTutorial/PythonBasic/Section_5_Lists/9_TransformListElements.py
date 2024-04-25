# in this tutorial, you’ll learn how to use the Python map() function with lists.
# when working with a list or a tuple, you often need to transform the elements of the list and return a new list that contains the transformed element
# suppose, you want to multiply every element in the list by 2, you can design a function to make it:
numbers = [1,2,3,4,5]
numbers_double = []

for number in numbers:
    numbers_double.append(number*2)
    
print(numbers_double)

# there is a nicer way to do this kind of task by using the map() built-in function
# the map() function iterates over all elements in a list, applies a function to each and returns a new iterator of the new elements
# the basic syntax of the map() function is as follows:
# iterator = map(function,list)
# in fact, you can pass any iterable to the map() function, not just a list or a tuple
# let's look at that example again:
numbers_test = [1,2,3,4,5]
def double_num(n):
    return n*2
numbers_double_test = list(map(double_num, numbers_test))
print(numbers_double_test)
# of course, you can also use lambda statement to make your code more concise

# take more examples:
# 1)using the Python map() function for a list of strings
names = ['david', 'peter', 'jenifer']
names_capitalize = list(map(lambda name:name.capitalize(),names))
print(names_capitalize)

# 2)using the Python map() function to a list of tuples:
price = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]
# suppose the output tuple has three parameters:["Name","price","tax"], and the tax is 10% of the original price
tax = list(map(lambda price:[price[0],price[1],price[1]*0.1],price))
print(tax)