# 【问题描述】

# 输入一个方形的长度和宽度，编写程序判断该方形是否为正方形（长和宽都应大于0）
# 【输入形式】

# 长度

# 宽度
# 【输出形式】

# （1）如果长度等于宽度，输出：It's a square

# （2）如果长度不等于宽度，输出：It's a rectangle

# （3）如果长或宽有小于0的，输出：illegal data

# 【样例输入1】

# 10

# 10
# 【样例输出1】

# It's a square

# 【样例输入2】

# -2

# 10
# 【样例输出2】

# illegal data

def judge(a,b):
    if a <= 0 or b <= 0:
        print("illegal data")
    elif a == b:
        print("It's a square")
    else:
        print("It's a rectangle")
        
a_test = int(input())
b_test = int(input())

judge(a_test,b_test)