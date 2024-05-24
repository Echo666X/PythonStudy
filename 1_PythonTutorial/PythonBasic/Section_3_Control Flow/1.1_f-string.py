#in the previous subchapter,we use "print(f"You'll pay ${ticket_price} for the ticket") "
#f-string is a way to format strings in Python that lets you directly reference variables and embed expressions in the string

#the basical syntax of the f-string is as follows:
# f"string{variable name or expression}"

#example
name = input()
print(f"Hello,{name}!")#Variable reference

x = 10
y = 100
print(f"The sum of {x} and {y} is {x+y}")#Quoted expression

def double(n):
    return n*2
print(f"Dounble of 5 is {double(5)}")#Call the function

pi = 3.1415926
print(f"Value of pi is {pi:.2f}")#Formatting numbers