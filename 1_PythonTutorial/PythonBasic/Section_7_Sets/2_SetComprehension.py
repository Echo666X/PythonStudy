# in this tutorial, you’ll learn how to use Python set comprehension to create a new set based on an existing one.
# suppose that you have a set of name in wrong capitalization and you want to get a new set consists of capitalized name
# you can use a for loop to make it:
names = {'KeVIN','mARy','ECHO'}
name_capitalized = set()
for name in names:
    name_capitalized.add(name.capitalize())
print(name_capitalized)
# to make it more elegent, you can use map() function and lambda expression
name_capitalized = set(map(lambda name:name.capitalize(),names))
print(name_capitalized)

# however, python provides you with the set comprehension syntax to make you code more concise
# the basic sytax of the set comprehension is as follows:
# {expression for element in set if condition}
# it should be note that the set comprehension returns a new set, it doesn't modify the original set
# back to the previous example, you can use the syntax in this way:
name_capitalized = {name.capitalize() for name in names}
print(name_capitalized)

# now suppose that 'ECHO' is not a name and you want to get a new set of the name in correct formatt
name_capitalized = {name.capitalize() for name in names if name.lower() != 'echo' }
print(name_capitalized)