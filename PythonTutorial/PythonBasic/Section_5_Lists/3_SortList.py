# in this tutorial, you’ll learn how to use the Python List sort() method to sort a list.

# the sort() method sorts the original list in place, which means the sort() method modifies the order of elements in the list
# the basical syntax of sort() is as follows:
list_test = [1,8,6,4,7,6,2,9]
list_test.sort()
print(list_test) 
# the output is [1, 2, 4, 6, 6, 7, 8, 9]
# it shows us that the sort() method sorts the elements using the less-than operator by default.
# if you want to sort the elements from higher to lower, you pass the reverse = True argument to the sort() method:
list_test.sort(reverse=True)
print(list_test)

# in addition to sorting numbers, the sort() method can be applied to many scenaries:
# 1)sort a list of strings
# the sort() method sorts the string elements alphabetically.
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort()
print(guests)
guests.sort(reverse=True)
print(guests)

#2)sort a list of tuples:
# this example will be sorted according to the company's revenue.
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

def revenue(company):
    return company[2]

companies.sort(key=revenue,reverse=True) # the key argument is used to specify a function that will be applied to each element in the list
print(companies)

# here you can use the lambda expression to make your code more concise.
companies_test = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

companies_test.sort(key=lambda company:company[2],reverse=True)
print(companies_test)

# if you don't want to modify the original list, you can use the sorted() function
# the usage of sorted() function is almost the same as the usage of the sort() function
# the basic syntax of the sorted() function is as follows:
# sorted(list, reverse=)
numbers_test = [5,89,4,3,6,7,6,21,8]
numbers_test1 = sorted(numbers_test,reverse=True)
print(numbers_test)
print(numbers_test1)
