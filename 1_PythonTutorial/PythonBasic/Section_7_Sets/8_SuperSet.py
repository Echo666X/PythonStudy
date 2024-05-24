# in this tutorial, you’ll learn how to use the Python issuperset() method to check if a set is a superset of another.
# if A is a superset of B, then B is a subset of A.
# to check if a srt a subset of another, you use the issupersetz() method to check if a set is a superset of another set
# logically, a set is a supersert of itself
# for example:
test_numbers = {1,2,8,6,9,4,3}
test_numbers_2 = {6,9,4}
print(test_numbers_2.issuperset(test_numbers))
print(test_numbers.issuperset(test_numbers_2))

# also you can use the superset operators (>=) to check is a set is a superset of another set
# and you can use the > to check if a set is a proper super set of another set
# for example:
test_numbers_3 = {1,2,3,4}
test_numbers_4 = {1,2,3,4}
print(test_numbers_3 >= test_numbers_4)
print(test_numbers_3>test_numbers_4)