# 输入平面上两个点A和B的坐标，(x1,y1)和(x2,y2)，完成如下任务：

# 要求使用者输入A,B的平面坐标共4个值;

# 计算并输出两点之间的距离，保留2位小数。


# 【输入形式】

# 点A的X坐标 , 点A的Y坐标
# 点B的X坐标 , 点B的Y坐标


# 【样例输入】

# 15,-189
# 22,176

# 【样例输出】

# 365.07
import math
def length(_x1,_y1,_x2,_y2):
    return math.sqrt((_x1-_x2)**2+(_y1-_y2)**2)

x1,y1 = map(float,input().split(","))
x2,y2 = map(float,input().split(","))

print(f"{length(x1,y1,x2,y2):.2f}")