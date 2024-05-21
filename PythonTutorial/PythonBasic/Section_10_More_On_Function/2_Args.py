# in this tutorial, you’ll learn about the Python *args parameters and how to use them for defining variadic functions.
# similarly, the following assigns 10 to x, 20 to y, and the lsit [30,40] to z
x,y,*z = [10,20,30,40]
print(f'x={x},y={y},z={z}')
# python uses the same concept for the function arguments,for examples:
def add(a,b,*c):
    '''the *c is a special arguments, 
    it's like tuple unpacking except that the args is a tuple, not a list '''
    total_abc = a + b
    for num in c:
        total_abc += num
    return total_abc

result_1 = add(10,20,30,40,50)
print(result_1)
# when  a function has a parameter preceded bt an asterisk(*), it can accept a variable number of arguments
# and you can pass zero, one, or more arguments to the *arg parameter
# in python, the parameters like *arg are called variadic parameters, the functions that have variadic parameters are called variadic functions
def output(*arg):
    print(type(arg))
    print(arg)
    print(arg[0]) # you can use the square bracket notation[] with an index to access each element of the args argument
output(1,2,3,4)
# the output is :
# <class 'tuple'>
# (1,2,3,4)
# 1

# also you can use a for loop to iterate over the elements of the tuple.
def total(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)

total(1,2,3,4) 

# it should be noted that once you use the *arg argument, you cannot add more positional arguments,
# however, you can use keyword arguments
def total_(*numbers,num):
    result_2 = num
    for number in numbers:
        result_2 += number
    print(result_2)
total_(1,2,3,4,num=5)

# unpacking arguments
def point(x,y):
    return f'{x},{y}'

test_a = (0,0)
# if you pass 'a' to the point function directly, it'll be a typeerror
output_test = point(*test_a)
print(output_test)