# in this tutorial, you’ll learn about Python modules, how to import objects from a module, and how to develop your modules.

# A module is a piece of software that has a specofic functionality
# every module has a name specified by the filename without the .py extension

# for example, in the 5_Type_Hints.py, we define a function "say_hi()", then you can use the import statement to use it:
# it should be noted that i have copied the files into the current folder, and i will explain the reason later
import test_5_Type_Hints
output = test_5_Type_Hints.say_hi("Kevin")
print(output)
# when you import a module, python executes all the code from the corresponding file

# you can use the import as statement to rename the module name to another as follows:
# import module as new_name

# if you want to reference objects in a module without prefixing the module name, you can explicitly import them using the following syntax:
# from module_name import function1, function2

# also you can rename an imported name to another by using the following import statement:
# from <module_name> import <name> as <new_name>

# to import every object from a module, you can use the following syntax:
# from module_name import *