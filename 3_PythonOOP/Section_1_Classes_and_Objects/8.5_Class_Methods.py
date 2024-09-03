# in this tutorial, you'll learn about Python class methods and when to use them appropriately.

# the instance methods are bound to a specific instance of a class
# they can access instance variables within the same class, to invoke instance methods, you need to create an instance of the class first

# the following defines the Person class:
class Person:
    def __init__(self,first_name,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def  get_full_name(self):
        return f'{self.first_name}{self.last_name}'
    
    def introduce(self):
        return f"Hi,I'm {self.first_name} {self.last_name}. I'm {self.age} years old."
    
    # suppose you want to add a method that creates an anonymous person to the Person class:
    # def create_anonymous(self):
    #    return Person('john','Doe',25)
    # the create_anonymous is an instance method that returns an anonymous person
    # however, to invoke the create_anonymous() method, you need to create an instance, which doesn't make sense in this case
    # that is why python class methods come into play
    
    # a class method isn't bound to any specific instance, it is bound to the class only
    # to define a class method:
    # first place the @classmethod decorator above the method definition, it will change an instance method to a class method
    # second rename the self parameter to cls. The cls means class, However, class is a keyword so you can use it as a parameter
    
    @classmethod
    def create_anonymous(cls):
        return Person('John', 'Doe', 25)
    # the create anonymous method cannot access instance attributes, but it can access class attributes via the cls variable
    
# to call a class method, you use the class name, followed by a dot, and then the method name like this:
# ClassName.method_name()
# for example:
anonymous = Person.create_anonymous()
print(anonymous.introduce())

# you can use class methods for any methods that are not bound to a specific instance but the class
# in practice, you often use class methods for methods that create an instance of the class

# when a method creates an instance of the class and return it, the method is called a factory method