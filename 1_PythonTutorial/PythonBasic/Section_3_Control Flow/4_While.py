# in this tutorial, you’ll learn about the Python while statement and how to use it to run a code block as long as a condition is true.
# Python while statement allows you to execute a code block rapidly as lonG as a condition is True

#the basical syntax of while is as follows:
#
#while condition:
#    body
#
#it should be noted that the condition ia an expression that evaluates to a boolean value

#"indefinite loop": you need to do something to stop the loop at some time, otherwise it will run forever
#"pretest loop": the while statement checks the condition at the beginning os each iteration

# now let us build a simple command line interactive program:

command = ""

while command.lower() != "quit":
    command = input("Please enter you command:")
    print(f"{command}")