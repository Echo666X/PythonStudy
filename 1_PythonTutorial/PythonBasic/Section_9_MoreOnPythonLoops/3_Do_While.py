# in this tutorial, you’ll learn how to emulate the do...while loop statement in Python
# a do...while loop statement executes at least one iteration, it checks the condition at the end of each iteration and executes a code block until the condition is False
# unfortunately, python doesn't support the do while loop. however, you can use the while loop and a break statement to emulate the do while loop statemet
# the basic structrue of the "do while" is as folllows:
# while True: # create an indefiniteloop
#   # code block
#   if confition:
#       break

# take a example to show the "do while
# suppose that you wnat to develop a number guessing game(the secret number is randomly generated)
from random import randint

min_number = 0
max_number = 10
attempt_times = 0

secret_num = randint(min_number,max_number) # the function of randint() is to return a random integer within the specified range (include bounds)
while True:
    input_num = int(input('please enter a number:'))
    attempt_times += 1
    if input_num > secret_num:
        print('it shoule be smaller')
    elif input_num < secret_num:
        print('it shoule be bigger')
    else:
        print(f'bingo! you have tried {attempt_times} times')
        break