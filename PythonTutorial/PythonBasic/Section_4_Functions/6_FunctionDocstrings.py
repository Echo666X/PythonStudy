# in this tutorial, you’ll learn about how to use docstrings to add documentation to a function.
# "help()" is a built-in function that allows you to show the documentation of a function

# to document your functions, you can use docstrings.
# when the first line in the function body is a string,Python will interpret it as a docstring.

def add(a,b):
    """add two arguments
    arguments a:an integer
    arguments b:an integer
    returns the sum of two arguments"""
    return a+b

print(add(5,6))
help(add)