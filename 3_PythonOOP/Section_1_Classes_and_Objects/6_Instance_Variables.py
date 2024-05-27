#  in this tutorial, you’ll learn about Python instance variables including data variables and function variables.


# introduction to the Python instance variables
# class variables are bound to a class while instance variables are bound to a specific instance of a class
# the instance variables are also called instance attributes
# the following defines a HtmlDocument class with two class variables:
from pprint import pprint

class HtmlDocument:
    version = 5
    extension = 'html'

pprint(HtmlDocument.__dict__)
pprint(HtmlDocument.version)
pprint(HtmlDocument.extension)
# in the output, the class variables are stored in the __dict__ attribute
# when you access the class variables via the class, python looks them up in the __dict__ of the class
# the following creates a new instance of the HtmlDocument class:
home = HtmlDocument() # the home is an instance of the HtmlDocument class, it has its own __dict__ attribute:
pprint(home.__dict__)

# unlike the __dict__ attribute of a class, the type of the __dict__ attribute of an instance is a dictionary
print(type(HtmlDocument.__dict__)) # the output is mappingproxy
print(type(home.__dict__)) # the output is dict

# since the dictionary is mutable, you can mutate it e.g., adding a new element to the dictionary
# python allows you to access the class variables from an instance of a class:
print(home.version) #5

# in this case, python looks up the variables extension and version in home.__dict__ first
# if it doesn't find them there, it will go up to the class and look up in the HtmlDocumenet.__dict__
# if python can find the variables in the __dict__ of the instance, it won't look further in the __dict__ of the class

# the following defines the version variable in the home object
home.version = 6
print(home.__dict__) #the __dict__ now contains one instance variable: {'version':6}
print(home.version) # the output is 6 instead 5

# if you change the class variables, these changes also reflect in the instances of the class:
HtmlDocument.media_type = 'text/html'
print(home.media_type) # text/html


# initializing instance variables
# in practice, you initialize instance variables for all instances of a class in the __init__ method
# for example, the following redefines the HtmlDocument class that has two instance variables name and contents
class HtmlDocument_1:
    version = 5
    extension = 'html'
    def __init__(self,name,contents) -> None:
        self.name = name
        self.contents = contents
        
# when creating a new instance of the HtmlDocument, you need to pass the corresponding arguments like this:
blank = HtmlDocument_1('Blank','')