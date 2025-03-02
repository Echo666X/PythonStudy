# in this tutorial, you’ll learn how to use the Python __repr__ dunder method and the difference between the __repr__ and __str__ methods.

# the __repr__ methods defines behavior when you pass an instance of a class to the repr()
# the __repr__ method returns the string representation of an object, 
# typically, the __repr__() returns a string that can be executed and yield the same value as the object

# start with the Person class:
from typing import Any


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
person = Person('John', 'Doe', 25)
print(repr(person)) # the output contains the memory address of the person object
print(type(repr(person))) # the type is string

# to customize the string representation of the object, you can implement the __repr__ method like this:
class Person1:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self) -> str:
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

person1 = Person1('John', 'Doe', 25)
# when you pass an instance of the Person class to the repr(), python will call the ___repr__ method automatically
print(repr(person1))
print(repr(Person("John","Doe",25))) # it return the person1 object

# when a class doesn't implement the __str__ method and you pass an instance of that class to the str(), 
# python returns the result of the __repr__  method because internally the __str__ method calls the __ repr__ method
# for example:
print(person1)

# if the class implement the __str__ method, python will call the __str__ method when you pass an instance of the class to the str()
# for example:
class Person2:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        return f'({self.first_name},{self.last_name},{self.age})'


person2 = Person2('John', 'Doe', 25)
# use str()
print(person2)

# use repr()
print(repr(person2))


# the main difference between __str__ and __repr__method is intended audiences
# the __str__ method returns a string representation of an object that is human-readable 
# while the __repr__method returns a string repesentation of an object that is machine-readable