# in this tutorial, you’ll learn how to unpack a list in Python to make your code more concise.

# if you want to assign the elements of the list to variables, a direct way is:
# variables1 = list[0]
# variables2 = list[1]

# however, Python provides a better way to do this, which called sequence unpacking
# basically, you can assign elements of a list or a tuple to multiple variables.
# for example:
colors = ['red','blue','green','black']
colors1,colors2,colors3,colors4 = colors
print(colors1,colors2,colors3,colors4,sep=",")
# however, the number of variables on the left side is the same as the number of elements in the list on the right side.

# if you want to unpack the first elements of a list and don't care the others, you can use the asterisk'*' in front of a variable name
# and the leftover elements will be packed into a list and assign them to a variable
colors_a,colors_b,*colors_other = colors
print(colors_a,colors_b,colors_other,sep=",")