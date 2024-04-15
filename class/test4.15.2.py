# 【问题描述】

#   输入飞机的名称、加速度a（米/秒的平方）和起飞速度v（米/秒)，根据以下公式计算飞机起飞所需要的最短跑道长度。

#   length=v*v/(2a)

# 【输入形式】

#   从键盘输入飞机名称、加速度a和起飞速度v，分https://programming.cqu.edu.cn/assignment/programList.jsp?proNum=3&courseID=1&assignID=1616&libCenter=false三行输入

# 【输出形式】

#  输出飞机的名称、加速度a、起飞速度v和最短跑道长度（结果保留2位小数)

# 【样例输入】

# B350

# 3.572

# 60

# 【样例输出】

# The acceleration of B350 is 3.57 M / s, the take-off speed is 60.00 M / s, and the shortest take-off runway length is 503.92 M.

def length(v,a):
    return v*v/(2*a)

name = input()
a = float(input())
v = float(input())

print(f"The acceleration of {name} is {a:.2f} M / s, the take-off speed is {v:.2f} M / s, and the shortest take-off runway length is {length(v,a):.2f} M.")