# In this tutorial, you’ll learn about Python partial functions and how to define partial functions using the partial function from the functools module.

# let's take an example to introduce the partial function:
def multiply(a,b):
    return a*b
def double(a):
    return multiply(a,2)

print(f"{double(2)}")
# the double function returns the multiply function, it passed the number 2 to the second argument of the multiply function
# as you can see, the double function reduces the arguments of the multiply function
# the double functions freezes the second arguments of the multiply function, which means it reduces the complexity of the multiply function
# in python, the double function is called a partial function


# since you will create partial functions sometimes, python provides you with the partial function from the functools standard module to help you define a partial functions
# the basic syntax of the partial function from the functools module is as follows:
# function.partial(fn,/,*args,**kwargs)
# the partial function returns new partial object, which is callable.
# the following example shows how to use partial function to make the previous code more clearly
from functools import partial

double_clear = partial(multiply,2) # when you call the double, python calls the multiply function where b argument defaults to 2
print(f"{double_clear(10)}")

x = 3
fn = partial(multiply,x)
print(f"{fn(10)}")