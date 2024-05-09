# 【问题描述】编写程序使用下列公式计算e。e=1+1/1!+1/2!+1/3!+…+1/n!

# 【输入形式】输入一个正整数n。

# 【输出形式】输出对应的e的值，结果保留小数点后六位有效数字

# 【样例输入】10

# 【样例输出】2.718282

def  main():
        num  =  eval(input())
        calculate_e(num)
        
def calculate_e(n):
    e = 1.0
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        e += 1 / factorial
    print("%.6f" % e)

main()
