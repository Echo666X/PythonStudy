# 【问题描述】求s=a+aa+aaa+aaaa+aaaaa+aa...a的值，其中a是一个数字，表示s由几个数相加。例如当a=3时，s等于三个数相加的和，即s=3+33+333=369。

# 【输入形式】从键盘输入一个正整数a。

# 【输出形式】输出此时s的值。

# 【样例输入1】3

# 【样例输出1】369

# 【样例输入2】10

# 【样例输出2】10203040506070809100

def  main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    result = 0
    current = a
    if a < 10:
        for _ in range(a):
            result += current
            current = current * 10 + a
        print(result)
    else:
        for _ in range(a):
            result += current
            current = current * 100 + a
        print(result)

main()