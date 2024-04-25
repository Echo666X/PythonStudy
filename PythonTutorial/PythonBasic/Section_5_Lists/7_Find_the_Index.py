# in this tutorial, you’ll learn how to find the index of an element in a list.

#  you use the index() function to find the index of an element in a lsit
# the basic syntax of the index() function is as follows:
# list.index()
cities = ['xian','beijing','chongqing','shanghai']
result = cities.index("xian")
print(result)
# if you attempt to find an element that doesn't exist in the list using the index() function, you'll get an error
# you can use the in operator to fix this issue:
city = "hongkong"
if city in cities:
    result_city = cities.index(city)
    print(result_city)
else:
    print(f"{city} doesn't exist in the list.")
