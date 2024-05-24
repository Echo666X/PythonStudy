# in this tutorial, you’ll learn about Python recursive functions and how to use them to simplify your code.
# a recursive function is a function that calls itself until it doesn't
# in programming, you will often find the recursive functions used in data structures and algorithms like trees, graphs, and binary searches

# it needs to have a condition to stop calling itself, so you need to add an if statement to stop it under a certain conditions
# the basic syntax of recursive functions is as follows:
# def fn():
#     # ...
#     if condition:
#         # stop calling itself
#     else:
#         fn()
#     # ...

# for example:
def count_down(start):
    """ Count down from a number  """
    print(start)
    start = start - 1
    if start > 0:
        count_down(start)
    
count_down(3)

def summation(n):
    if n > 0:
        return n + summation(n-1)
    else:
        return 0
print(summation(3))

# if you use the  ternary operator, the code will be much cleaner.
def sum_cleaner(n):
    return n + sum_cleaner(n-1) if n>0 else 0

print(sum_cleaner(5))