# in this tutorial, you’ll learn about the Python try...except...finally statement.
# the tyr...except statement also has an optional clause called finally
# the finally clase always executes whether an exception occurs or not, it executes after the try clause and any except clause
# for example:
a,b = map(float,input().split(','))
try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print("the value of b is zero!")
finally:
    print('finishing up.')
# if you enter "8,0", it returns "the value of b is zero""finishing up."
# the except clause is optional, which means you can just use try and finally