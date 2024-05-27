# in this tutorial, you’ll learn about Python classes and objects and how to define a new class.


# objects
# an objects is a container that contains data and functionality
# the data represents the object at a particular moment in time, therefore, the data of an object is called the state
    # python uses attributes to model the state of an object
# the functionality represents the behaviors of an object, python uses function to model the behaviors, 
    # when a function is associated with an object, it becomes a method of the object

# in other words, an object is a container that contains the state and methods
# before creating objects, you define a class first, and from the class, you can create one or more objects
# the objects of a class are also called instances of a class.


# to define a class in python, you use the class keyword followed by the classname and a colon
class Person:
    pass
# by convention, you use capitalized names for classes, if the class name contains multiple words, you use the CalmCase format
# to create an instance of a class, you use the class name with parenthese like this:
person = Person()
print(person) # the output is its name and memory address
# to get an identity of an object, you use the id() function:
print(id(person))  # the id of an object is unique, also you can use the hex() function to return the integer returned by the id() function to a lowercase hexadecimal string prefixed with 0x:
# you can use the isinstance() function to judge whether an object is an instance of a class:
print(isinstance(person,Person))  # the output is True


# a class is also an object in Python
# everything in python is an object, including classes
# for example, once you define the Person class, python creates an object with the name Person, the person object has attributes,
# you can find its name using the __name__ attribute:
print(Person.__name__) # name

# also the person object has the type of 'type'
print(type(Person))