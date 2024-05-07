
# 【问题描述】折半查找。 1 个列表里存储了 20 个子列表， 各子列表内存储了学生的学号及姓名两个元素， 两个元素都是字符串类型。 现已知该 20 个学生子列表已按学号递增序排好序。请设计一个程序， 使用折半查找算法通过最少次数的比较找到指定学号的学生， 如果有， 输出这个学生的学号和姓名， 如果没有， 输出报告未找到该学生。 列表中存储数据为stu_list=

# [['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

# ['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

# ['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

# ['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

# ['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]

# 【输入形式】输入要查找的学生学号
# 【输出形式】输出学号和姓名
# 【样例输入】201800
# 【样例输出】None

# 【样例输入】201803
# 【样例输出】201803zhangsan

stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],

['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],

['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],

['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],

['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]

num_input = input()
num_output = [num for num in stu_list if num[0] == num_input ]
num_test_output = str(num_output)
num_test1_output = num_test_output[3:9]
num_test2_output = num_test_output[13:-3]
result = f"{num_test1_output}{num_test2_output}"
    
if result != '':
    print(result)
else:
    print('None')