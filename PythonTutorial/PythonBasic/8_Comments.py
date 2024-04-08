# in this tutorial, you’ll learn how to add comments to your code. And you’ll learn various kinds of Python comments including block comments, inline comments, and documentation string.
# Typically,you use comments to explain formulas,algorithms,and complex business logic

# Python block comments &inline comments
# just use a sigle #
num1 = 1 #balabala

print(num1)
#Python docstrings
#Unlike a regular comment, a documentation string can be accessed at run-time
#using  obj.__doc__ attribute where obj is the name of the function.

#However,docstrings are not the comments in typically speaking
#They create anonymous variables,they're not ignored by the Python interpreter

# 1) One- line docstrings
def quicksort():
    """sort the list using quicksort algorithm """
def increase():
    """
    balabala
    """
    