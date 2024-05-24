# in this tutorial, you’ll learn about the Python type hints and how to use the mypy tool to check types statically.

# some programming languages have static typing, which means you need to declare types of variables, parameters and return values of a function upfront
 # the predefined typs allow the compliers to check the code before compiling and running the program

# however, python uses dynamic typing, in which a function's variables, parameters and return values can be any type
 # the types of variables can change while the program runs
# generally, dynamic typing makes it easy to program and causes unexpected errors that you can only discover until the program runs

# python's type hints provide you with optional static typing to leverage the best of both static and dynamic typing
# the basic syntax of adding type hints to a parameter and return value of a function is as follows:
# parameter : type ->type

# for example, the following program shows how to use type hints in a function which accepts a string and returns another string
def say_hi(name:str) -> str:
    return f'hi,{name}!'

output_1 = say_hi("Kevin")
print(output_1)

# besides the str type, you can use other built-in types such as int, float, bool and bytes for type hintings
# it should be noted that the python interpreter ignoresb type hints completely, for example, if you pass a number to the say_hi() function, the program will run without any warning or error

# using a static type checker tool: mypy
# python does not have an official static type checker tool, at the moment,the most popular third-party tool is Mypy
# you can pass the following command in the TERMINAL to install mypy
# pip install mypy


# adding type hints for multiple types
# suppose you want design a funtion returns the sum of two numbers which are parameters, however, they can be integers or floats
# you can use the module to set type hints for multiple types
from typing import Union 
# after import the Union, you can use the Union to create a union type that includes int and float
def add(x:Union[int, float],y:Union[int, float] ) -> Union[int, float]: # it should be noted that the basic syntax of the Union method is Union(type_1,type_2) 
    return x+y
# additionally, from Python 3.10, you can use the X|Y syntax to create a union type
def add_test(x:int|float, y:int|float) -> int|float :
    return x+y


# python allows you to assign an alias to a type and use alias for type hintings.
# for example:
type_num = Union[int,float]

def add_test_2(a:type_num,b:type_num) -> type_num:
    return a+b


# adding type hints for lists, dictionaries and sets
# you can use the following built-in types to set the type hints for a dictionary, list and set
# for example, you can type hints in a variable as a list:
rating : list = [1,2,3]
# however, once you type hints in "rating", you cannot assign a dictionary or set to it later, or you will get an error


# you can use Type_alias method to specify the types of values in the list, dictionary, and sets
# for example, you can use type_alias method to define a list of integers
from typing import List
rating_int : List[int] = [1,2,3,4]
print(rating_int)
# you can find the details of typing module in 5.1.md


# if a function doesn't explicitly return  a value, you can use None to type hint the return value
def log(message:str) -> None:
    print(message)