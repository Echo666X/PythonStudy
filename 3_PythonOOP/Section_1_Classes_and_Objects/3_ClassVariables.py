# in this tutorial, you’ll learn how the Python class variables (or attributes) work.
# as the previous chapter said, a class is an object in python

# class variables are bound to the class, they are shared by all instances of that class
# the following example adds the extension and version class variables to the HtmlDocument class
class HtmlDocument:
    extension = 'html'
    version = '5'
# both extension and the version are the class variables of the HtmlDocument class, they are bound to the HtmlDocument class


# get the values of class variables
# to get the values of class variables, you can use the dot notation(.)
print(HtmlDocument.extension)
# if you access a class variable that does not exist, you will get an attributeError exception

# another way to get the value of a class variable is to use the getattr() function, this function accepts an object and a variable name
print(getattr(HtmlDocument,'extension'))
# however, if the class variable doesn't exist, you will also get an exception, to avoid the exception, you can specify a default value
print(getattr(HtmlDocument,'media_type','text/html'))
print(getattr(HtmlDocument,'extension','3')) # the output is 'html'


# set values for class variables
# to set a value for a class variable, you use the dot notation:
HtmlDocument.version = 10
print(getattr(HtmlDocument,'version'))
# also you can use the setattr() built-in function:
setattr(HtmlDocument,'version',10)
print(getattr(HtmlDocument,'version'))
# since python is a dynamic language, you can add a class variable to a class at runtime after you have created it
# for example, the following adds the media_type class variable to the HtmlDocument class:
HtmlDocument.media_type = 'text_html'
print(getattr(HtmlDocument,'media_type'))


# delete class variable:
# to delete a class variable at runtime, you use the delattr() function:
delattr(HtmlDocument,'media_type')
# also you can use the del keyword:
del HtmlDocument.version


# class variable storage:
# python store class variables in the __dict__ attribute, the __dict__ is a mapping proxy, which is a mapping proxy, for example:
from pprint import pprint
pprint(HtmlDocument.__dict__)
# it should be noted that python doesnot allow you to change the __dict__ directly
# however you can access class variables through the __dict__ dictionary:
print(HtmlDocument.__dict__['extension']) 


# callable class attributes
# class attributes can be any object such as a function, when you add a function to a class, the function becomes a class attribute
# since a function is callable, the class attribute is called a callable class attribute