# 【问题描述】

# 输入一个整数列表和整数n(n可以是负数）和正整数m，从该列表中选择第n个元素，把该元素重复m次，然后放到列表的尾端，最后输出列表。如果输入的n值不在列表下标范围之内，则输出"error"
# 【输入形式】

# 输入时，第一行输入列表的元素，用英文逗号分隔。

# 第二行输入两个数字n和m，用英文逗号分隔。

# 【输出形式】

# 直接使用print输出列表
# 【样例输入1】

# 1,2,3,4,5

# 2,3
# 【样例输出1】

# [1, 2, 3, 4, 5, 3, 3, 3]

# 【样例输入2】

# 1,2,3,4,5

# 5,3
# 【样例输出2】

# error

try:
    list_ = list(map(int,input().split(',')))
    n,m = map(int,input().split(','))
    if n>0:
        for list_ in range(0,m):
            list_.append(list_[n])
    else:
        n += len(list_)
        for list_ in range(0,m):
            list_.append(list_[n])
    print(list_)
except IndexError:
    print('error')
