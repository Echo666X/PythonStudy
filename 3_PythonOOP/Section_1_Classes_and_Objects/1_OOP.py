#  in this tutorial, you’ll learn object-oriented programming in Python, 
# including essential concepts such as objects, classes, attributes, methods, inheritances, overriding methods, etc.

# everything in python is an object, an object has a state and behaviors.
# to create an object, you define a class first, and then, from a class, you can create one or more objects, the objects are instances of a class

# you use the class keyword followed by the class name to define a class:
class Class_Name:
    pass
# to create an object from the Class_Name, you use the class name followed by (), just like calling a function
object_name = Class_Name() #it shoule be noted that classes are callable


# define instance attributes
# python is dynamic, it means that you can add an attribute to an instance of a class dynamically
# we define a class called "Person" and then adds a name attribute to the person object
class Person:
    pass

person = Person()
person.name = 'Kevin'
# however, if you create another Person object, the new object will not have the name attribute


# to define and initialize an attribute for all instances of a class, you use the __init__ method.
# the following defines the Person class with two instance attributes name and age.
class Person_1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
# when you create a Person object, python automatically calls the __init__ method to initialize the instance attributes.
# in the __init__ method,the self is the instance of the Person class
person_1 = Person_1('Kevin',19)
# to access an instance attribute, you use the dot notation.
# for example:
print(f"{person_1.age}") # the person_1.name returns the value of the name attribute of the person object


# define instance methods:
class Person_2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def say_hi(self):
        return f"Hi,{self.name}"
# to call an instance method, you also use the dot notation, for example:
person_2 = Person_2(name='John',age='19')
print(person_2.say_hi())
    
    
# define class attributes
# unlike instance attributes, class attributes are shared by all instances of the class
# they are helpful if you want to define class constants or variables that keep track of the number of instances of a class
# take an example:
class Person_3:
    counter = 0
    
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        Person_3.counter += 1 # once an object is created, the value of the counter increase 1

person_3_1 = Person_3('Mary',19)
print(person_3_1.counter) # the output is 1
person_3_2 = Person_3('Lily',19)
print(person_3_2.counter) # the output is 2


# define class method
# class method is shared by all instances of the class
# the first argument of a class method is the class itself.
# by convention, its name is cls. Python automatically passes this argument to the class method
# also, you use the @classmethod decorator to decorate a class method
class Person_4:
    counter = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person_4.counter +=1
    def greet(self):
        return f"Hi, it's {self.name}."
    
    @classmethod
    def create_anoymous(cls):
        return Person_4('Anoymous',00)
    
Anoymous_person = Person_4.create_anoymous()
print(Anoymous_person.name)


# define static method
# a static method is not bound to a class or any instances of the class.
# in python, you use static methods to group logically related functions in a class
# you use the @staticmethod decorator to define a static method
# the following example defines a class TemperatureConverter that has two static methods that convert from celsius to fahrenheit and vice versa
class TemperatureConverter:
    @staticmethod
    def c_to_f(c):
        return 9*c/5+32
    
    @staticmethod
    def f_to_c(f):
        return 5*(f-32)/9
# to call a static method, you use the ClassName.static_method_name() syntax, for example:
f_output = TemperatureConverter.c_to_f(30)
print(f_output)


# single inheritance
# a class can reuse another class by inheriting it, when a child class inherits from a parent class, the child class can access the attributes and methods of the parent class
# for example, you can define an Employee class that inherits from the Person_4 class:
class Employee(Person_4):
    def __init__(self, name, age, job_title):  # the employee class extends the person_4 class by adding one more attribute called job_title
        super().__init__(name, age)  # the super() methods allows a child class to access a method of the parent class
        self.job_title = job_title
        
    # to override the greet() method in the Person class, you can define the greet() method in the employee class as follows:
    def greet(self):
        return super().greet() + f'i am a {self.job_title}' 
employee = Employee('Kevin','19','killer')
print(employee.greet())