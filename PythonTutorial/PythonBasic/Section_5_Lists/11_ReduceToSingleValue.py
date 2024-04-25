# in this tutorial, you’ll learn how to use the Python reduce() function to reduce a list into a single value.\
# sometimes, you want to reduce a list to a single value, suppose that you want to calculate the sum of all elements in a number list:
# you can use a for loop to make it
numbers = [1,84,65,25,79,99,6565,6]
sum_num = 0
for number in numbers:
    sum_num += number
    
print(sum_num)
# however, Python provides a function called reduce() that allows you to reduce a list in a more concise way
# the basic syntax of the reduce() function is as follows:
# reduce(function,list)
# it should be noted that the reduce() function is not a built-in functions, in fact, it belongs to the functools module
# to use these funcntion, you need to import it from the functools module
import functools
numbers_reduce = [1,84,65,25,79,99,6565,6]
numbers_reduce_test = functools.reduce(lambda a,b:a+b,numbers_reduce)
print(numbers_reduce_test)