# in this tutorial, you’ll learn about disjoint sets and how to use the Python isdisjoint() method to check if two sets are disjoint.
# two sets are disjoint when they have no elements in common
# in other words, two disjoint sets are sets whose intersection is an empty set
# you can use isdisjoint() method to check if two sets are disjoint or not
# the disjoint() method can accept any iterable, not just a set, if you pass a list, a tuple, or a dictionary, the isdisjoint() method will convert it to a set before checking
# take an example:
odd_numbers = {1,3,5,7}
even_numbers = {2,4,6,8}
print(odd_numbers.isdisjoint(even_numbers))