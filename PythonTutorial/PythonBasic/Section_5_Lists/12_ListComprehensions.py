# in this tutorial, you’ll learn about Python List comprehensions that allow you to create a new list from an existing one.

# in programming, you often need to transform elements of a list and return a new list
# for example, suppose that you have a list of numbers and you want to get a new list of squares based on this list
# you can use a for loop to make it:
numbers = [1,2,3,4,5]
numbers_squares = []
for numeber in numbers:
    numbers_squares.append(numeber**2)
print(numbers_squares)
# to make it more concise, you can use the map() function
numbers_squares = list(map(lambda number:number**2,numbers))
print(numbers_squares)
# however, the above method isn't really concise and beautiful
# to help you create a list based on the transformation of elements of an existing list, Python provides a feature called list comprehensions
numbers_squares_comprehension = [number ** 2 for number in numbers]
print(numbers_squares_comprehension)

# an list comprehension consists of the following parts:
# 1)an input list:numbers
# 2)a variable that represents the elements of the list:number
# 3)an output expression that returns the elements of the output list from the element of the input list

# the basic syntax of the list comprehension is as follows:
# [output_expression for element in input_list]
# it's equivalent to the following :
# output_list = []
# for element in list:
#   output_list.append(output_expression)

mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]
highest_height = max(m[1] for m in mountains)
highest_mountains = [m for m in mountains if m[1] == highest_height]
print(highest_mountains)