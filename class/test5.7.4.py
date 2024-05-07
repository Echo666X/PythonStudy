# 【问题描述】有一个分数数列：2/1,3/2,5/3,8/5,13/8,21/13,...,从键盘输入一个正整数n，求出这个数列的前n项之和。

# 【输入形式】输入一个正整数n。

# 【输出形式】输出该数列的前n项之和，并保留四位小数。

# 【样例输入】3

# 【样例输出】5.1667

def caculate(n):
    num1 = 2.0
    num2 = 1.0
    total_num =0.0
    for _ in range(n):
        total_num += num1 / num2
        num1,num2 = num1+num2,num1
    return total_num

num_input = int(input())
result = caculate(num_input)
print(f"{result:.4f}")