# in this tutorial, you’ll learn about the Python for loop and how to use it to execute a code block a fixed number of times.
# in programming,you often want to execute a block of code multiple times,
# to do so,you use a for loop

#the basical syntax of for loop is as follows:
#
# for index in range(n):
#     statement
#
#in this syntax, the index is called a loop counter,and n is the number of times that the loop will execute the statement

#the range() function:
#the basical syntax of range() is as follows: range(start,stop,step)##by default,start == 0, step ==1
print(list(range(1,10,1)))

for index in range(1,5,1):
    print(index)
    
total = 0
for num in range(1,101):
    total += num
print(total)