# in this tutorial, you’ll learn about the Python hash() function and how to override the __hash__ method in a custom class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 22)
p2 = Person('Jane', 22)

print(hash(p1))
print(hash(p2))
# the hash() function accepts an object and returns the hash value as an integer.
# whe you pass an object to the hash() function, python will execute the __hash__ special method of the object

# if a class overrides the __eq__method, the objects of the class become unhashable, which means that you won't able to use the objects in a mapping type
# to make the class hashable, you also need to implement the __hash__ method
def __eq__(self, other):
    return isinstance(other, Person) and self.age == other.age
def __hash__(self):
    return hash(self.age)

Person.__eq__ = __eq__
Person.__hash__ = __hash__