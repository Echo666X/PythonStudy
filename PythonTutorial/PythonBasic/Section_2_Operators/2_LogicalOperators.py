#in this tutorial, you’ll learn about Python logical operators and how to use them to combine multiple conditions.
#Python has three Logical Operators: and or not

#The and operators
n1 = 9.999
print(n1>9 and n1>10)
#the condition a and b only returns True if both conditions evaluate to True

#The or operators
print(n1>9 or n1<10)
#the condition a or b only return Flase if both conditions evaluate to False

#The not operators
print(not (n1>9 and n1>10))
#The not operators applies to one condition,it reverses the result of that condition

# When you mix the logical operators,there will be a precedence of logical operators
#"not"is high,"and" is medium,"or" is low
#Python will group the operands for the oprators with the highest precedence first,
#then group the lower precedence,and so on 

# For example, a or b and c-------means a or (b and c)
# not a and b or c------means ((not a) and b) or c