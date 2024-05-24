def  leapyear(x):
      
    if (x % 400 == 0) or (x % 4 == 0 and x % 100 != 0):
        return True
    else:
        return False

year=int(input())
if  leapyear(year):
    print("闰年")
else:
    print("平年")