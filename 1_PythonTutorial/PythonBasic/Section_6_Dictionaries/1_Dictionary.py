# in this tutorial, you’ll learn about Python Dictionary which allows you to organize related information.
# a dictionary is a collection of key- value pairs where each key is associated with a value
# the value in the key-value pairs can be a number, a string, a list, a tuple or even another dictionary
# the ke in the key-value pairs must be immutable, it cannot be changed, for example, a number, a string, a tuple

# you can use curly braces {} to define a dictionary, inside the curly braces, you can place zero, one, or mant key-value pairs
# typically, you define an empty dictonary before a loop, either for loop or while loop, and inside the loop, you add key-value pairs to the dictionary
# the basic syntax of a dictonary is as follows:
# dict_name = {}
# to access a value by key from a dictionary, you can use the square bracket notation[] or the get() method
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
print(person['first_name'])
last_name_test = person.get('last_name')
print(last_name_test)
# if the key of the value you want to access doesn't exist, the get() method returns None but the square bracket will throw a KeyError
# the get() method also returns a default value when the key doesn't exist by passing the default value to its second argument
test_value = person.get("former_name","0_0000_0000")
print(test_value)

# although the key is immutable, the dictionry itself can be changed, in other words, the dictionary has a dymatic structure, 
# so you can add new key-value pairs to a dictionary at any time, you specify the name of the dictionary followed by thr new key in square brackets along with the new value
# for example:
person['former_name'] = 'Kevin'
test_value = person.get("former_name","0_0000_0000")
print(test_value)

# also you can modify the values in a key-value pair, you specify the dictionary name with the key in square brackets and the new value associated with the key
person['age'] = 26
print(person)

# if you want to remove a key-value pair by a key, you use the del statement: del dict[key]
del person['former_name']
print(person)


# looping through a dictionary
# 1)looping all key-value pairs in a dictionary
# python dictionary provides a method called items() that returns an object which contains a list of key-value pairs as tuples in a list
print(person.items())
# to iterate over all key-value pairs in a dictionary, you use a for loop with two variable kay and value to unpack each tuple of the list
for key,value in person.items():
    print(f"{key}:{value}")

# 2)sometimes, you just want to loop through all keys in a dictionary, you can use a for loop with the keys() method in this case
for key in person.keys():
    print(key)
    
# 3)same as above, you can use the values() method to return a list of values without any keys
for value in person.values():
    print(value)

# in python, you can use ** to unpack a few dictionaries and insert its contents into another dictionary
# this is typically used for merging dictionaries
# for example:
test_dict_1 = {'a':1,'b':2}
test_dict_2 = {'c':3,'d':4}
new_dict = {**test_dict_1,**test_dict_2}
print(new_dict)