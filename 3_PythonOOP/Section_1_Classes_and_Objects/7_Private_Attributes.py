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