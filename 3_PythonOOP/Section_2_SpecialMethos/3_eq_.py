# in this tutorial, you’ll learn how to use the Python __eq__ method to compare two objects by their values.

# suppose that you have the following person class with three instance attributes and you create two instances of the person class:
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
Jonn = Person('John','Doe',25)
Jane = Person('Jane','Doe',25)

# in this example, john and jane are not same
print(Jonn == Jane)
# since they have the same age, you want them to be equal, in other word, you want the following expression to return True: John == Jane

# to do it, you can implement the _eq_ dunder method in the Person class:
def __eq__(self,other):
    return self.age == other.age
Person.__eq__ = __eq__
print(Jonn == Jane)