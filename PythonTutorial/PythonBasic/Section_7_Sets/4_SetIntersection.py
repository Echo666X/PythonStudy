# in this tutorial, you’ll learn about the Python set intersection and how to use it to intersect two or more sets.
# it is similar to fet a union, you can use intersection() method or set intersection operator &
# for example:
Kevin_skills = {'C++','Java','C#'}
Mary_skills  = {'C','C++','Java'}
skills = Kevin_skills.intersection(Mary_skills)
print(skills)
skills = Kevin_skills & Mary_skills
print(skills)

# similarly, the intersection() can accept any iterables but the intersection operator can only accepts sets