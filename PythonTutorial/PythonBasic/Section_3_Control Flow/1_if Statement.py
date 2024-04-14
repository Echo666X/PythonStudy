# in this tutorial, you’ll learn how to use the Python if statement to execute a block of code based on a condition.


#if statement:
#the basical syntax of the if statement is as follows:
# if condition:
# if-block

# note that the colon that follows the condition is very important
age  = int(input('please enter your age:'))
if age >= 18:
    print("(test1)you're able to enter.")

#it should be noted that the indentation is very important
#if you don't use the indentation correctly ,the program will work differently

if age >= 18:
    print("(test2)you're able to enter.")
print("(test2)this line will appear no matter what the age")



#if ... else statement
#the basical syntax of the if else statement is as follows:
# if condition:
#     if-block;
# else:
#     else-block;

if age >= 18:
    print("(test3)you're able to enter.")
else:
    print("(test3)you can not enter")
    


#if elif else 
#the basical syntax of the if elif else statement is as follows:
# if if-condition:
#     if-block
# elif elif-condition1:
#     elif-block1
# elif elif-condition2:
#     elif-block2
# ...
# else:
#     else-block

if age >=18:
    ticket_price = 100
elif age<18 and age>=14:
    ticket_price = 80
elif age<14 and age>=10:
    ticket_price = 60
else:
    ticket_price = 0
    
print(f"You'll pay ${ticket_price} for the ticket") 
#f-string: string formatting
#the next subchapter will show this in detail