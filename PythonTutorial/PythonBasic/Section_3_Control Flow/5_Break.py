# in this tutorial, you’ll learn about the Python break statement and how to use it to exit a loop prematurely.
# sometimes you want to terminate a loop prematurely regardless of the results of the conditional tests
# typically, you use the break statement with if statement to terminate a loop when a condition is true

for index in range(0,10,2):
    index += index
    if index >= 10:
        break
    print(index,end=" ")
# the output is 0 4 8
    
#when you use the break statement in the nested loop,it will terminate the innermost loop:
for x in range(0,10,2):
    for y in range (2):
        if y >1:
            break
        print(f"({x},{y})")
    
#you can use the break statement in the while loop similarly:
while True:
    color = input("please enter your favorite clor:")
    if color.lower() == "quit":
        break