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
def max_number(digits):
    # 将列表中的数字按从大到小排序
    digits.sort(reverse=True)
    # 将排好序的数字连接成一个整数
    max_num = int(''.join(map(str, digits)))
    return max_num

# 读取输入的列表
input_list = input()
# 解析列表字符串，并转换为列表
digits = eval(input_list)
# 调用函数获取最大整数
result = max_number(digits)
# 输出结果
print(result)
