# in this tutorial, you’ll learn how to use the Python try...except statement to handle exceptions gracefully.
# there are two main kinds of errors in python: syntax errors and exceptions
# when you write an invaid python code, you'll get a syntax error, even though when you code has valid syntax, it may cause an error during execution
# errors that occur during the execution are called exceptions, the causes of exceptions mainly come from the environment where the code executes
# for examples, it may because: reading a file that doesn't exist, connecting to a remote server that is offline, or bad user inputs
# when an exception occurs, the program doesn't handle it automatically, this results in an error message
# for examples:
test_numbers = float(input("enter a test number:"))
print(test_numbers)
# if you enter a 200', it will return a exception:
# # enter a test number:120''
# # Traceback (most recent call last):
# #   File "d:\Code\Python\PythonStudy\PythonTutorial\PythonBasic\Section_8_ExceptionHandling\1_Try_Except.py", line 8, in <module>
# #     test_numbers = float(input("enter a test number:"))
# #                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # ValueError: could not convert string to float: "120''"
# because the float() couldn't convert the string 200' to a number, the python interpreter issued a ValueError exception
# in python, exceptions have different types such as TypeError, NameError, etc

# to make the program more robust,you need to handle the exception once it occurs, in other words, you need to catch the exceptions and inform users so that they can fix ir
# a good way to handle this is not to show what the python interpreter returns.
# instead, you replace that error message with a more user-friendly one.
# to do that, you can use the Python try...except statement:
# try:
#     #code that may cause error
# except:
#     # handle errors
# the statement in try will execute first, if no exception occurs, the except clause is skipped and the execution of the try statement is completed
# if an exception occurs at any statement in the try clause, the rest of the clause is skipped and the except clause is executed
try:
    test_numbers_1 = float(input("please enter a number:"))
    print(test_numbers_1)
# if you just use except, there will be a warning:No exception type(s) specified
# to catch a selected exception, you should place the type of exception after the except keyword
except ValueError as e:
    print("Error! The number you entered is untrue")
    
# the try...except allows you to handle multiple exceptions by specifying multiple except clauses:
#
# try:
#     # code that may cause an exception
# except Exception1 as e1:
#     # handle exception
# except Exception2 as e2:
#     # handle exception
# except Exception3 as e3:
#     # handle exception 
#
# this allows you to respond to each type of exception differently
# if you want to have the same response to some types of exceptions, you can group them into one except clause:
# 
# try:
#     # code that may cause an exception
# except (Exception1, Exception2):
#     # handle exception

# here is a complete example:
try:
    # get input net sales
    print('Enter the net sales for')

    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)
except ValueError :
    print('Error! Please enter a number for net sales.')
except ZeroDivisionError:
    print('Error! The prior net sales cannot be zero.')
