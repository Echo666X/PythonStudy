# in this tutorial, you’ll learn about Python Set type and how to use it effectively.
# a python set is an unordered list of immutable elements, it means:
# elements in a set are unordered.
# elements in a set are unique, a set doesn't allow duplicate elements
# elements in a set cannot be changed, for example, they can be numbers, strings, and tuples, but cannot be lists or dictionaries

# to define a set, you use the curly brace{}, the basic syntax of the set is as follows:
# set_name = {elements1,elements2,elements3}

# as you can see, the set and the dictionary are both use the curly braces, therefore, you need to do something to distinguish them
# for example, an empty item in a dictionary can be created as "empty_dict = {}" but in a set it should be created as empty_set = set()
# the set() function is a built-in function
# it should be noted that an empty set evaluates to False in boolean context
empty_set = set()
if not empty_set:
    print("an empty set valuates to False in boolean context")
    
# in fact, you can pass an iterable to the set() function to create a set.
# for example, you can pass a list which is an iterable to the set() function like this:
skills = set(['Problem solving','Critical Thinking'])
print(skills)
# note that the original order of elements may not be preserved

# if an iterable has duplicate elements, the set() function will remove them.
char = set(["letter"])# in order to distinguish with the following text, this means that 'letter' is stored in the set as a completes string element
print(char)
char = set("letter")# this means each character in the string acts as an indepenfent element of the set
print(char)

# you can use the built-in function len() function to get the number of elements in a set
number_char = len(char)
print(number_char)

# you can use the in operator to check if a set contains an element: element in set
# the in operator returns True if the set contains the element, otherwise it returns False, and you can use the not operator to negate the in operator
test_numbers = {1,4,8,2,5}
if 9  not in test_numbers:
    print("number9 is not in the test_numbers")
    
# you can use the add() method to add an element to a set: set.add(element)
test_numbers.add(9)
if 9  in test_numbers:
    print("number9 is in the test_numbers")

# use the remove() method to remove an element from a set
test_numbers.remove(9)
output_test = lambda: "number9 is in the test_number" if 9 in test_numbers else "number9 is not in the test_numbers"
print(output_test())
# however, if the element you want to remove is not in the set, there will be a Keyerror
# to avoid this, you can use in operator to check if the element you want to remove is in the set
# to make it more convenient, the set has the discard() method that allows you to remove an element no matter it's in the set or not
test_numbers.discard(10)
print(test_numbers)

# you can use the pop() method to remove and return an element from a set
test_numbers.pop()
print(test_numbers)
# it should be noted that because the set is unordered, the pop() method removes an unspecified element from a set,
# if you execute the pop multiple times, it'll show a different value each time
# and you can use clear() method to remove all elements from a set.

# to make a set immutable, you use the built-in function called frozenset(), it will return a new immutable set from an existing one
test_numbers = frozenset(test_numbers)
# after this, if you want to change the element in the set, you'll get an error

# since a set is iterable, you can use a for loop to iterate over its elements
name_test = {'Echo','Kevin','Mary','Lily'}
for name in name_test:
    print(name,end=",")
print()    
# and you can use the bulit-in function enumerate() function to access the  index of the current element inside the loop
for index,name in enumerate(name_test):
    print(f"{index},{name};",end="  ")
# it should be noted that evert time you run the code, you'll get the set elements in a different order