# in this tutorial, you’ll learn about the Python continue statement and how to use it to control the loop.
# the continue statement is used inside a for loop or a while loop
# it will skips the current iteration and starts the next one.

#the basical syntax is as follows(if-based):
# for index in range(n):
#     if condition:
#        continue
#     # more code here

#this example will show how to display even numbers from 0 - 9
for num in range(0,10):
    if num % 2 != 0:
        continue
    print(num)