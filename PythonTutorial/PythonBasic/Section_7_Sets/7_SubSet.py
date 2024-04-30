# in this tutorial, you’ll learn about how to use the Python issubset() method to check if a set is a subset of another set.
# suppose that you have two sets A and B if all elements of A are also elements of B, the, set B is a superset of set A
# you can use the set issubset() method to check if a set is a subset of another
# the basic syntax of the issubset() method is as follows:
# set_1.issubset(set_2)
# if the set_1 is a subset of the set_2, the issubset() method returns True, Otherwise it returns False
test_numbers = {1,2,8,6,9,4,3}
test_numbers_2 = {6,9,4}
print(test_numbers_2.issubset(test_numbers))
# by  definition, a set is also a subset of itself

# besides using the issubset() method, you can sue the subset operator (<=) to check if a set is a subset of another set
print(test_numbers <= test_numbers_2)
# the proper subset operator (<) check if the set_1 is a proper subset of the set_2
test_numbers_3 = {6,9,4}
print(test_numbers_2<test_numbers_3)