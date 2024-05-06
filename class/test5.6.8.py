# 【问题描述】输入一个整数，输出小于等于该整数的所有水仙花数，每行输出一个，若没有水仙花数则输出“none”

# “3位水仙花数”是指一个三位整数，其各位数字的3次方和等于该数本身。例如：ABC是一个“3位水仙花数”，则：A的3次方＋B的3次方＋C的3次方 = ABC。 

# 【输入形式】

        
# 【输出形式】

        
# 【样例输入】

# 100
# 【样例输出】

# none
def is_armstrong(num):
    # 计算各位数字的立方和
    digit1 = num // 100
    digit2 = (num // 10) % 10
    digit3 = num % 10
    armstrong_sum = digit1 ** 3 + digit2 ** 3 + digit3 ** 3

    # 判断是否为水仙花数
    return armstrong_sum == num

# 输入整数
num_input = int(input())

# 用于标记是否找到水仙花数
found = False

# 遍历范围从100到输入整数
start = 100 if num_input >= 100 else num_input
stop = 1000 if num_input >1000 else num_input+1
for num in range(start, stop):
    if is_armstrong(num):
        print(num)
        found = True

# 如果没有找到水仙花数，输出 "none"
if not found:
    print("none", end="")
