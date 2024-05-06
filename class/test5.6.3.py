# 【问题描述】

# 在一个赌博用的转盘上，口袋的编号是从0到36，口袋的颜色如下： 

# 从1号袋到10号袋，奇数的口袋是红色，偶数的口袋是黑色。

# 从11号袋到18号袋，奇数的口袋是黑色，偶数的口袋是红色。

# 从19号袋到28号袋，奇数的口袋是红色，偶数的口袋是黑色。 

# 从29号袋到36号袋，奇数的口袋是黑色，偶数的口袋是红色。

# 0号口袋是绿色

# 请编写一个程序，根据用户输入的口袋编号，输出口袋的颜色。 如果用户输入的数字不在0~36这个范围内，则输出“error”。

# 【输入形式】
# 整数

# 【输出形式】

# green or red or black or error
# 【样例输入1】

# 0
# 【样例输出1】

# green

# 【样例输入2】

# 11
# 【样例输出2】

# black

color_dict = {
    0:'green',
    **{i:'red' if i%2 == 1 else 'black' for i in range(1,11)},
    **{i:'black' if i%2 == 1 else 'red' for i in range(11,19)},
    **{i:'red' if i%2 == 1 else 'black' for i in range(19,29)},
    **{i:'black' if i%2 == 1 else 'red' for i in range(29,37)},   
}

key_input = int(input())
color_output = color_dict.get(key_input,'error')
print(color_output)