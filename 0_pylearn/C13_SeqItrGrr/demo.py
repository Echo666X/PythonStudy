class CountedSet(set):
    pass

s = CountedSet()
s.add("a")
s.add("c")
s.add("a")
a = s.getCount("a")   #a值应为2
c = s.getCount("c")   #c值应为1
