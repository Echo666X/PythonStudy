# 【问题描述】

# 编程实现学校评奖系统，（1）如果数学成绩大于等于99并且语文成绩大于等于99，获奖学金500。

# （2）如果数学和语文成绩都小于30，输出重修。
# 【输入形式】

# 语文成绩

# 数学成绩
# 【输出形式】

# （1）如果数学和语文成绩都大于等于99，输出:You won a scholarship of 500 yuan!

# （2）如果数学和语文成绩都小于30，输出:You need to relearn!

# 【样例输入】

# 100

# 99
# 【样例输出】

# You won a scholarship of 500 yuan!

def award(chinese,math):
    "编程实现学校评奖系统"
    if chinese >= 99 and math >= 99:
        print("You won a scholarship of 500 yuan!")
    elif chinese < 30 and math < 30:
        print("You need to relearn!")
n1 = int(input())
n2 = int(input())

award(n1,n2)