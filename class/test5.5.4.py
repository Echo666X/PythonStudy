# 【问题描述】

# 读入一个整数列表，输出删除最大元素和最小元素后的列表。最大元素和最小元素可能有多个。
# 【输入形式】

# 输入列表，包括方括号
# 【输出形式】

# 直接用print输出列表
# 【样例输入】

# [1,2,3,4,5,6,1,7,7]
# 【样例输出】

# [2, 3, 4, 5, 6]

list_test = list(map(int,input()[1:-1].split(',')))
max_ele = max(list_test)
min_ele = min(list_test)
list_final = []
for ele in list_test[::1]:
    if ele != max_ele and ele != min_ele:
        list_final.append(ele)
print(list_final)
        