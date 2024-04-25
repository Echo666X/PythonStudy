# in this tutorial, you’ll learn about Python list slice and how to use it to manipulate lists effectively.

# to get a sublist, you use the slice notation, which allows you to get a sublist from a list.
# the basic syntax of list slice is as follows:
# sub_list = list[start:end:step]

# you can see the introduction to string slice in test4.20.3, the string slicing is similar to the list slicing
# start: the start index defaults to 0 (inclusive)
# end: the end index defaults to the length of the list.(not included)
# step: the step index defaults to 1.
# the value can be positive or negative, the positive values slice the list from the first element to the last element while negative values slice on the contrary

colors_test = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(colors_test[1:4])

# if you want to get the n-first elements from a list, you omit the first argument:
numbers = [1,2,3,4,5,6,7]
print(numbers[:4])

# if you want to get the n-last elements from a list, you use the negative indexes
print(numbers[-4:])

# if you want to get every nth element from a list, you use the step to return a sublist
print(numbers[::2])

# you can also use list slicing to reverse a list
print(numbers[::-1])

# besides extracting a part of a list, the list slice allows you to change the list element
# if you want to substitute part of list:
numbers[0:2] = [0,1]
print(numbers)
numbers[0:2] = [1,2]

#similarly, you can replace and resize a list in this way.
print(f"the length of numbers-list is {len(numbers)}")
numbers[0:2] = [0,1,2]
print(f"the length of numbers-list is {len(numbers)}")

#also you can delete elements:
del numbers[0:2]
print(numbers)