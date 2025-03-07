# in this tutorial, you’ll learn about the Python property class and how to use it to define properties for a class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person('John', 18)
# since age is the instance attribute of the Person class, you can assign it a new value:
john.age = 19
# The following assignment is also technically valid:
john.age = -1
# however, the age is semantically valid
# To fix it, you can define a pair of methods called getter and setter.

# The getter and setter methods provide an interface for accessing an instance attribute:
# The getter returns the value of an attribute
# The setter sets a new value for an attribute

# In our example, you can make the attribute private (by convention) and define a getter and a setter to manipulate the attribute.ageage
# for example:
class Person_0:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age
    
# This code works just fine. But it has a backward compatibility issue.
# Suppose you released the class for a while and other developers have been already using it. And now you add the getter and setter, all the code that uses the Person won’t work anymore.Person
# To define a getter and setter method while achieving backward compatibility, you can use the class.property()

# the property class returns a object, it has the following syntax:
# property(fget=None, fset=None, fdel=None, doc=None)
# fget is a function to get the value of the attribute, or the getter method.
# fset is a function to set the value of the attribute, or the setter method.
# fdel is a function to delete the attribute.
# doc is a docstring i.e., a comment.
class Person_1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self.age = age

    def get_age(self):
        return self.age

    age = property(fget=get_age, fset=set_age)
# note that it is a class attribute not an instance attribute