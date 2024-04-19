# in this tutorial, you’ll learn to develop Python functions by using the def keyword.
# a function is a named code block that performs a job or returns a value
# in practice,you use functions to divide a large program into smaller and more manageable parts
# the functions will make you program easier to develop, read, test, and maintain

#the basical form of funtion is as follows:
def greet():
    """Display a greeting to users"""
    print("hi")
#after the definition,when you want to use a function, you need to call it.
#to call a function, you write the function's name,followed by the information that the function needs in parenthese
#for example:
greet()

# you can also pass some information to the function
def happy_birthday(name):
    print(f"happy birth day,{name}!")
name1 = input("please enter your name:")
happy_birthday(name1)

#besides, you can also return a value

def total(a,b):
    return a+b
num1,num2 = map(int,input("please enter the number:").split(","))
print(total(num1,num2))