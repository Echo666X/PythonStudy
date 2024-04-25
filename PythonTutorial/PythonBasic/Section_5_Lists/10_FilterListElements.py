# in this tutorial, you’ll learn how to filter list elements by using the built-in Python filter() function.

# sometimes, you need to iterate over elements of a list and select some of them based on specified criteria
# suppose that you want to select elements greater than a certain value from a list, you can use a for loop to make it
scores = [20,80,98,45,60,71]
scores_selected = []
for score in scores:
    if score >=50:
        scores_selected.append(score)
scores_selected.sort()
print(scores_selected)
# however, Python has a built-in function called filter() that allows you to filter a list in a more beautiful way
# the basic syntax of the filter() function is as follows:
# filter(function,list)
# the filter() function iterates over the elements of the list and applies the function to each element
# it returns an iterator for the elements where the function() returns True
# same as the map() function, you can pass any iterable to the second argument of the filter() function, not just a list
# let's look at that example again:
scores_filter = [20,80,98,45,60,71]
scores_filter_selected = list(filter(lambda score:score>=50 , scores_filter))
scores_filter_selected.sort()
print(scores_filter_selected)