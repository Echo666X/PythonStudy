# in this tutorial, you’ll learn about Python tuples and how to use them effectively.
# sometimes you want to create a list of items that cannot be changed throughout the program, tuples allows you to do that.
# so by definition, a tuple is an immutable list.

# the tuple is like a list except that it uses parenthese() instead of square brackets[]
rgb = ('red','green','blue')
# once defining a tuple, you can access an individual element by its index:   
print(rgb[0],rgb[1],rgb[2],sep=",")
# since a tuple is immutable, the element cannot be change.

# if you want to define a tuple with one element, you need to include a trailing comma after the first element.
numbers = (3,) 
print(type(numbers)) #the type of numbers is tuple
numbers_test = (3)
print(type(numbers_test))# however, the type of number_test is int

# even though you can not change a tuple, you can assign a new tuple to a variable that references a tuple
colors = ('red', 'green', 'blue')
print(colors)
colors = ('Cyan', 'Magenta', 'Yellow', 'black')
print(colors)