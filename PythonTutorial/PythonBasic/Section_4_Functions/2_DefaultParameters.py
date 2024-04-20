# in this tutorial, you’ll learn about the Python default parameters to simplify function calls.

# when you define a function, you can specify a default value for each parameter
# the basic syntax of default parameters is as follows:
# def function_name(param1, param2=value2, param3=value3, ...):

# when you call a function and pass an argument to the parameter that already has a default value
# the function will use that argument instead of the default value
# if you dont pass the argument, the function will use the default value

# it should be noted that, you need to place parameters with the default values after other parameters
# othewise, you will get a syntax error

# for example
def greet(name, message='Hi'):
    return f"{message} {name}"

print(greet("Echo666X"))

# when you use mutiple parameters, things will change
def greet_name(name_ = "there",message_ = "Hi"):
    return f"{message_} {name_}"

print(greet_name(message_="hello")) 
#if there is nothing on the left_hand side of the equal sign, the greet_name function will treat "hello" as the first argument,not the second one
