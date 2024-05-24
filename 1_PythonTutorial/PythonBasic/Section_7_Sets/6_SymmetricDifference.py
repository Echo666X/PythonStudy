# in this tutorial, you’ll learn how to find the symmetric difference between two or more sets in Python.
# the symmetric difference between two sets is a set of elements that are in either set, but not in their intersection
# the symmetric difference includes the difference between s1_s2 and the difference between s2_s1
# same as the last few verses, you can use the symmetric_difference() method or the symmetric difference operator (^)
Kevin_skills = {'C++','Java','C#'}
Mary_skills  = {'C','C++','Java'}
symmetric = Kevin_skills.symmetric_difference(Mary_skills)
print(symmetric)

# and the symmetric() method can accept one or more iterables that can be strings，lists or dictionaries
# but the symmetric operator can only apply to sets