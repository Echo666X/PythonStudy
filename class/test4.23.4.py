# 【问题描述】

# 本题要求编写程序输入一个百分制成绩并把其转换为五分制成绩输出。

# 转换规则为：

# 大于等于90分为A； 小于90且大于等于80为B； 小于80且大于等于70为C； 小于70且大于等于60为D； 小于60为E。

# 【输入形式】输入只有一个百分制成绩，如98.5

# 【输出形式】输出对应的五分制成绩，如A

# 【样例输入1】67

# 【样例输出1】D

# 【样例输入2】94.5

# 【样例输出2】A

level = ("A","B","C","D","E")

def level_judge(n):
    if n >= 90:
        print(level[0])
    elif n < 90 and n >= 80:
        print(level[1])
    elif n < 80 and n >= 70:
        print(level[2])
    elif n < 70 and n >= 60:
        print(level[3])
    else:
        print(level[4])
        
grade = float(input())
level_judge(grade)
        