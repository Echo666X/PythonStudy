# in this tutorial, you’ll learn about encapsulation and how to use private attributes to accomplish encapsulation in Python.

# introduction to encapsulation in python:
# encapsulation is one of four fundamental concepts in OOP including abstraction, encapsulation, inheritance and polymorphism
# encapsulation is the packing of the data and functions that works on that data within a single object
# by doing so, you can hide the internal state of the object from the outside
# this is known as information hiding

# a class is an example of encapsulation, a class bundles data and methods into a single unit
# and a class provides the access to its attributes via methods

# the idea of information hiding is that if you have an attribute that isn't visible to the outside
# you can control the access to its value to make sure your object is always has a valid state

# let's take some examples:

# the following defines the Counter class:
class Counter:
    def __init__(self) -> None:
        self.current = 0
    def increment(self):
        self.current += 1
    def value(self):
        return self.current
    def reset(self):
        self.current = 0
        
counter = Counter()

counter.increment()
counter.increment()
counter.increment()

print(counter.value()) # the output is 3

# however, this program still has one issue.
# from the outside of the Counter class, you still can access the current attribute and change it to whatever you want
# for example:
counter.increment()
counter.increment()
counter.current = 999

print(counter.value()) # the output is 999

# in order to prevent the current attribute from modifying outside of the Counter class
# the private attributes come into playdef 


# private attributes
# private attributes can be only accessible from the methods of the class
# in other words, they cannot be accessible from outside of the class

# python doesn't have a concept of private attributes, in other words, all attributes are accessible from the outside of a class
# by convention, you can define a private attribute by prefixing a single underscore: _attribute
# for example:
class PrivatecCounter:
    def __init__(self) -> None:
        self._current = 0  # the _current is a private attribute
    def increment(self):
        self._current += 1
    def value(self):
        return self._current
    def reset(self):
        self._current = 0
        
counter = Counter()

counter.increment()
counter.increment()

print(f'{counter.value()}')
# such properties are renamed by the python interpreter, making them inaccessible directly from outside


# name mangling with double underscores
# if you prefix an attribute name with double underscores(__), 
# python will automatically change the name of the __attribute to:
# _class__attribute
# which is called the name mangling in python

# by doing this, you cannot access the __attribute directly from the outside of a class like: instance.__attribute
# however, you still can access it using the _class__attribute name:
# instance._class__attribute
# for example:
class CounterNameMangling:
    def __init__(self) -> None:
        self.__current = 0
    def increment(self):
        self.__current += 1
    def value(self):
        return self.__current
    def reset(self):
        self.__current = 0

counter_1 = CounterNameMangling()
# now, if you attempt to access __current attribute like this: counter.__current
# you will get an error
# however, you can access the __current attribute as _Counter__attribute:
print(counter_1._CounterNameMangling__current)