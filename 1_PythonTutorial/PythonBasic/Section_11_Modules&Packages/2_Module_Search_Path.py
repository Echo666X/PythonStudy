# in this tutorial, you’ll learn how the module search path works in Python when you import a module into a program.
# when you import a module in a programm, python will search for the module.py file from the following source:
    # the currenr folder from which the program executes
    # a list of folders specified in the PYTHONPATH environment variable, if you set it before
    # an installation-dependent list of folders that you configured when you installed python
    
# python stores the resulting search path in the sys.path variable that comes from the sys module
# the following program shows the current module search path:
import sys

for path in sys.path:
    print(path)