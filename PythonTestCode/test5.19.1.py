x,y = map(float,input().split(','))

if x>0:
    if y>0:
        print('第1象限')
    elif y <0:
        print('第4象限')
elif x<0:
    if y>0:
        print('第2象限')
    elif y <0:
        print('第3象限')