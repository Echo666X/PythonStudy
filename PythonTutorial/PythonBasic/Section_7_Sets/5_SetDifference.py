# in this tutorial, you’ll learn about the Python Set difference and how to use it to find the difference between two or more sets.
# the difference between the set_1 and the set_2 means that the elements in the difference_set are in set_1 but not in the set_2
# it should be noted that the set deffrence is not commutative, which means the difference between s1 & s2 is not equal to the difference between s2 &s1
# same as the last few verses, you can use the set difference() method or set difference operator (-) to find the difference between sets
Kevin_skills = {'C++','Java','C#'}
Mary_skills  = {'C','C++','Java'}
set_K_to_M = Kevin_skills.difference(Mary_skills)
set_M_to_K = Mary_skills - Kevin_skills
print(set_K_to_M)
print(set_M_to_K)

# similarly, the difference() method can accept one or more itreales while the set difference operator can only allow set
