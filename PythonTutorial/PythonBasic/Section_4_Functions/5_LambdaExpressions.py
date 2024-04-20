# in this tutorial, you’ll learn about Python lambda expressions and how to use them to write anonymous functions.
# sometimes, you need to write a simple function that contains one expression.However,you need to use this function once,
# and it will unnnessary to define that function with the def keyword, so the lambda expressions come into play.

# anoymous functions are functions without names.
# def anoymous(parameters):
#    return expression
# the above is equivalent to the following:
# lambda parameters: expression
# and that is the basic syntax of the lambda expressions

# Functions that accept a function example
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


full_name = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{first_name} {last_name}"
)
print(full_name)

full_name = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{last_name} {first_name}"
)
print(full_name)

# Functions that return a function example
def times(n):
    return lambda x,y:(x+y)/n
double = times(2)
print(double(2,3))

# lambda in a loop
callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())
