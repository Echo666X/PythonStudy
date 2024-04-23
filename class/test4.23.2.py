# 【问题描述】

# 读入一个正整数列表，每个正整数都只有一位。把这些列表里面的数字，按位数组织成一个最大的整数，每个数字占据一位，不能重复使用。然后输出这个数字。例如列表[1,2,3,4] 可以组成1234, 或者4321等多个整数。输出最大整数。
# 【输入形式】

# 一个包含一位自然数的列表
# 【输出形式】

# 整数
# 【样例输入】

# [0,1,2,3,2]
# 【样例输出】

# 32210

list_test = list(map(int,input()[1:-1].split(',')))

list_test.sort()

final_num = ''

while list_test:
    max_num = str(list_test.pop())
    final_num += max_num

if final_num[0] == '0':
    print(0)
else:
    print(final_num)