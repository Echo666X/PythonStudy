# in this tutorial, you will learn how to use the Python __str__ method to make a string representation of a class

# start with the Person class:
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
person = Person('John','Doe','25')
print(person)
# the output is the memory address of the instance

# sometimes it's useful to have a string represnetation of an instance of a class
# to customize the string representation of a class instance,the class needs to implement the __str__ magic method

# the following illustrates how to implement the __str__ method in the person class
class Person_1:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self) -> str:
        return f'Person({self.first_name},{self.last_name},{self.age})'
    
person = Person_1('John', 'Doe', 25)
print(person)