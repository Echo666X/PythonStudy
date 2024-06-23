# in this tutorial, you’ll learn about the Python class attributes and when to use them appropriately.


# introduction to class attributes
# start with a simple example:
class Circle:
    def __init__(self,radius) -> None:
        self.pi = 3.1415926
        self.radius = radius
        
    def area(self):
        return self.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * self.pi * self.radius
    
    # the circle has two attributes pi and radius, it also has two methods that calculate the area and circumference of a circle
    # both pi and radius are called instance attributes, they belong to a specific instance of the circle class, if you change the attributes of an instance, it won't affect other instances
    
# besides instance attributes, python also supports class attributes, the class attributes don't associate with any specific instance of the class, but the are shared by all instance of the class

# to define a class attribute, you place it outside of the __init__() method, for example:
class Circle_1:
    pi = 3.1415926
    def __init__(self,radius) -> None:
        self.radius = radius
    
    def area(self):
        return self.pi * self.radius ** 2
    
    def circumference (self):
        return 2 * self.pi *self.radius
    
