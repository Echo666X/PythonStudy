# 【问题描述】

# 输入一个整数列表，计算所有元素的平均值，如果结果中小数为0，请只输出整数部分，如果结果中的小数部分不为0，则输出结果保留两位小数。
# 【输入形式】

# 从键盘输入列表，包含方括号，列表元素用逗号分隔。

# 【输出形式】

# 纯整数，或者带两位小数的浮点数
# 【样例输入1】

# [1,2,3,4,5]
# 【样例输出1】

# 3

# 【样例输入2】

# [2,2,3,7,5,1]
# 【样例输出2】

# 3.33
import functools
numbers = list(map(float,input()[1:-1].split(',')))
numbers_sum = functools.reduce(lambda a,b:a+b,numbers)
numbers_num = len(numbers)
finally_num = float(numbers_sum/numbers_num)
if finally_num.is_integer() == True:
    print(f'{int(finally_num)}')
else:
    print(f'{finally_num:.2f}')