# 【问题描述】

# 考拉兹猜想（Collatz conjecture）又称奇偶归一猜想，是指对于每一个正整数，如果它是奇数，则对它乘3再加1,如果它是偶数，则对它除以2。 如此循环，最终都能得到1。编写一个程序，输入一个正整数，打印其考拉兹序列。

# 【输入形式】

# 1个>1的正整数

# 【输出形式】

# 以逗号分隔的考拉兹序列。

# 【样例输入】

# 5
# 【样例输出】

# 16,8,4,2,1

def collatz_sequence(n):
    sequence = [] 
    while n != 1:
        if n % 2 == 0:
            n //= 2 
        else:
            n = 3 * n + 1
        sequence.append(n)  
    return ','.join(map(str, sequence)) 

user_input = int(input())
print(collatz_sequence(user_input))

