# in this tutorial, you’ll learn how to use the Python for loop to iterate over a list in Python.

# the basical syntax of using python for loop to iterate over a lisrt is as follows:
# for item in list:
#   process the item
# in this syntax, the for loop statement assigns an individual element of the list to the item variable in each iteration

# for example:
cities = ['beijing','xian','shanghai','chongqing']
for city in cities:
    print(city)
    
# sometimes, you may want to access indexes of elements inside the loop, in this case, you can use the enumerate() function

# it will return a tuple that contains the current index and element of the list
# the basical syntax of the enumerate function is as follows:
# enumerate(iterable,start = 0)
# iterable represents an iterable object, such as a list, tuple, string, etc
# start represents the starting index value, the default is 0
for item in enumerate(cities):
    print(item)
# to access the index, you can unpack the tuple within the for loop statement:
for index, city in enumerate(cities,start=1):
    print(f"{index}: {city}")