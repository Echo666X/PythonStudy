# in this tutorial, you’ll learn about Python List type and how to manipulate list elements effectively.
# a list is an ordered collection of items

# the basic syntax of list is as follows:
# list_name = [item1,item2,item3,...]
# the items can be numbers, strings or other lists


# Lists are zero-based indexes, in other words, the first element has an index pf 0, and the second element has an index of1
# for example:
numbers = [1,2,3,4]
print(numbers[1]) #the out put is 2
print(numbers[-1]) # the negative index allows you to access elements starting from the end of the lists.


# a list is dynamic, which means you can modify elements in the list, add new elements to the list, and remove elements from a list
# the following example shows how to change first element of the numbers list to 10
numbers_test_1 = [1,3,5,7,9]
numbers_test_1[0] = 10
print(numbers_test_1) 
# and you can also multiply elements by numbers:
numbers_test_1[1] = numbers_test_1[1]*2
print(numbers_test_1)
numbers_test_1[2] /= 2
print(numbers_test_1)

# besides modification, you can also add elements to the lists or remove from them

# the append() method can append an element to the end of a list:
numbers_test_2 = [1,2,3,4,5,6]
numbers_test_2.append(7)
print(numbers_test_2)

# the insert() method adds a new element at any position in the list
numbers_test_2.insert(0,0)
print(numbers_test_2)

# the del statement allows you to remove an element from a list by specifying the position of the element
numbers_test_3 = [1,2,3,4]
del numbers_test_3[0]
print(numbers_test_3)

# the pop() method removes the last element from a list and returns that element:
last_in_test_3 = numbers_test_3.pop()
print(last_in_test_3)
print(numbers_test_3)
# typically, you can insert the location index of the element in pop() to remove the element from the list but still access the value of that element

# to remove an element by value, you use remove() method.
# it should be noted that the remove() method removes only the first element it encounters in the list
numbers_test_4 = [1,2,3,3,4]
numbers_test_4.remove(3)
print(numbers_test_4)