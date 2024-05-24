#in this tutorial, you’ll learn about type conversion in Python and some useful type conversion functions.

#input()  function

    #the input() function returns a string, not an integer.
    # For example
    # price = input('Enter the price ($):')
    # tax = input('Enter the tax rate (%):')

    # tax_amount = price * tax / 100

    # print(f'The tax amount price is ${tax_amount}')


    #To solve this question,use int() function
    #it just like C:int(),double(),to implement a temporary transformation
    # For example
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

tax_amount = int(price) * int(tax) / 100

print(f'The tax amount price is ${tax_amount}')
    # Besides the int() function,Py supports other type conversion
    #float(str) – convert a string to a floating-point number.
    # bool(val) – convert a value to a boolean value, either True or False.
    # str(val) – return the string representation of a value.

#type(value) function
#use it to get the type of a value