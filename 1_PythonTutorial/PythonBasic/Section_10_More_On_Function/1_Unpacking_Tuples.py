# in this tutorial, you’ll learn how to unpack tuples in Python.

# reviewing python tuples:
# in practice, python defines a tuple using commas, not parentheses
# python also uses the paretheses to create an empty tuple
# to define a tuple with only one element, you still need to use a comma, for example,(1,) is a tuple but the (1) is an integer

# unpacking the tuple:
x,y = 1,2
print(type(1))# the output is int
x = 1,2
print(type(x))# the output is tuple

# you can use the method above to swap values of teo variables:
a = int(input())
b = int(input())
# traditionally,you would use a temporary variable to swap, more mathematically, you can swap a and b in this way
print(f"a={a},b={b}")
a = a + b
b = a - b
a = a - b
print(f"a={a},b={b}")
# howver, you can use the unpacking tuple syntax to achieve it in a more beautiful way
x,y = map(int,input().split(','))
print(f'x={x},y={y}')
x,y = y,x
print(f'x={x},y={y}')

# however, if the number of values on the right is different from the number of variables on the left,it'll result in an error
# to fix it, you can add a _ variable, _ is a regular variable in python, by convention, it's called a dummy variable
# for example: 
a,b,_ = 10,4,2


# sometimes, you don't want to unpack every single item in a tuple, in this case, you can use the * operator to extend unpacking
num1, num2, *num_rest = (1,6,8,6,2,87)
# it should be noted that you can only use the * operator once on the left-hand

# python also allows you to use the * operator to unpack those tuples and merge them into a single tuple
odd_numbers = (1,3,5,7,9)
even_numbers = (2,4,6,8)
numbers = (*odd_numbers,*even_numbers)