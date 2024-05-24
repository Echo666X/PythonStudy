# in this tutorial, you’ll learn how to union two or more sets by using the Python set union() or set union operator (|).
# the union of two set returns a new set that contains distinct elements from both sets
# the basic syntax of union() method is as follows:
# new_set = set.union(another_set,...)
# for example:
num1 = {1,3,6,8,5}
num2 = {89,62,447,51,91,3,6,48,15}
union_num = num1.union(num2)
print(union_num)

# also you can use set union operator | to union two sets
union_num = num1|num2
print(union_num)

# in fact, the union() method accepts one or more iterables, converts the iterables to sets and performs the union
num3 = {89,62,447,51,91,3,6,48,15} # a tuples
num4 = {1,3,6,8,5} # a set
union_num = num3.union(num4)
print(union_num)
# however the union operator only allows sets, not iterables like the union() method