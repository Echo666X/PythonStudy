# in this tutorial, you’ll learn about the Python iterables and iterators.
# an iterable is an object that includes 0,1 or many elements, it has the ability to return its elements one at a time

# the range() function is an iterable because you can iterate over its result:
for index in range(3):
    print(index)
    
# a string is an iterable, you can use a for loop to iterate over it:
string = "interables"
for ch in string:
    print(ch)    
    
# lists nd tuples are also iterables because you can loop over them:
ranks = ["a","b","c"]
for rank in ranks:
    print(rank)
# the rule of thumb is that if you know if can loop over somethin, it's interable

# an iterable can be iterated over, and an iterator is the agent that performs the iteration
# you can use the iter() function to get an iterator from an iterable
colors = ["red","blue","yellow","green","black"]
colors_iter = iter(colors)
# once you have an iterator, you can use the next() function to get the next element from the iterable 
# every time you call the next() function, it returns the next element in the iterables
colors_iter_test = next(colors_iter)
print(colors_iter_test)
colors_iter_test = next(colors_iter)
print(colors_iter_test)
colors_iter_test = next(colors_iter)
print(colors_iter_test)
# if there isn't any more element and you still call the next() function, it will issue an exception

# it should be noted that the iterator is stateful, which means once you consume an element from the itrator, it's gone
# in other word, the iterator becomes empty once you complete looping over an itretor.
# since you can interate over an iterator, the iterator is also an iterable object.
# for example:
colors_test = ["red","blue","yellow","green","black"]
itretor = iter(colors_test)

for color in itretor:
    print(color)

