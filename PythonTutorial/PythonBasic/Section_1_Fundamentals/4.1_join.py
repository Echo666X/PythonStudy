# in this tutorial, you will learn about the join() method
# the join() method comes in handy when you have a list with multiple elements and want to concatenate the elements into a string
# it is a string method that concatenates elements in a list and returns a string
# the basic syntax of the join() method is as follows:
# string.join(iterable)
# where string is the string used to concatenate elements, and iterable is the iterable object to be concatenated, usually a list
# for example:
fruit_list = ["apple", "banana", "cherry"]
result = '-'.join(fruit_list)
print(result)
