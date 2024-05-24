# 【问题描述】

# 编写一个程序，用户输入一个值x，计算分段函数f(x)的值并输出结果，函数f(x)请用自定义函数实现。

# 其中，

# image.png

# 【输入形式】

# x
# 【输出形式】

# 小数点后2位
# 【样例输入】

# 21.5
# 【样例输出】

# 2.12
import math

def funtion(x):
    if x<20:
        print(f"{(6*x*x+1):.2f}")
    elif x >=20 and x < 40:
        print(f"{(math.sqrt(3*x-60)):.2f}") 
    elif x >= 40:
        print(f"{(100/(x+1)):.2f}")
    
num = float(input())
funtion(num)