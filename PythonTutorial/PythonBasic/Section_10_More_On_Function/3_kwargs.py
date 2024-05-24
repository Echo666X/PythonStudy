# in this tutorial, you’ll learn about the Python **kwargs parameters.
# in python, a function can have a parameter preceded by two stars(**), 
# the **kwargs is called a keyword parameter
# when a function has the **kwargs parameter, it can accept a variable number of key arguments as a dictionary


# the following example defines a function called connect() that accepts a **kwargs parameter
def connect(**kwargs):
    print(type(kwargs))
    print(kwargs)

connect()
connect(sever = "localhost",port = 3306, user = "root", password = "Python") # in the connect() functionm, you can use the argument as a dictionary
# also you can pass a dictionary to the function, you need to add ** to the argument like this:
config = {"sever" : "localhost",
          "port" : 3306, 
          'user' : "root", 
          "password": "Python"}
connect(**config)


# it should be noted that if a function has the **kwargs parameter and other parameters, you need to place the **kwargs after other parameters
# otherwise, you will get an error
# for example, function(arg,**kwargs) is correct but the function(**kwargs, arg) will causes a SytaxError


# if you want to use both *args and **kwargs arguments, you can use the syntax like: fn(*args, **kwargs)
# the fn function can accept a variable number of the positional arguments, Python will pack them as a tuple and assign the tuple to the args argument
# the fn function also accepts a variable number of keyword arguments, python will pack them as a dictionary and assign the dictionary to the kwarg argument
# for example:
def function(*arg,**kwargs):
    print(arg)
    print(kwargs)
    
function(1,2,x=10,y=20)