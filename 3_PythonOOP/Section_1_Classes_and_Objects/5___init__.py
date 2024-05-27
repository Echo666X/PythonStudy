# in this tutorial, you’ll learn how to use the Python __init__() method to initialize object’s attributes.


# introduction
# when you create a new object of a class, python automatically calls the __init__() method to initialize the object's attributes
 # unlike regular methods, the __init__() method has two underscores on each side, therefore, this method is often called dunder init
 # the name comes abbreviation of the double underscores init
# the double underscores at both sides of the __init__() method indicate that python will use the method internally
# in other words, you should not explictly call this method

# since python will automatically call the __init__() method immediately after creating a new object, you can use the __init__() method to initialize the object's attributes
# the following defines the Person class with the __init__() method
class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
if __name__ == '__main__':
    person = Person('John',25)
    print(f'he is {person.name},he is {person.age} years old')
# when you create an instance of the Person c;ass, python performs two thing:
    # 1) create a new instance of the Person class by setting the object's namespace such as __dict__ attribute to empty {}
    # 2) call the __init__method to initialize the attributes of the newly created object
    
# it should be noted that the __init__ method doesn't create the object but only initializes the object's attributes
# hence, the __init__() is not a constructor

# if the __init__ has parameters other than the self, you need to pass the corresponding arguments when creating a new object
# otherwise, you will get an error


# the __init__ method with default parameters 
# the __init__() method's parameters can have default values
class Person_22:
    def __init__(self,name,age = 22) -> None:
        self.name = name
        self.age = age

person_22 = Person_22('John')
print(f' i am {person_22.name}, i am {person_22.age} years old.')