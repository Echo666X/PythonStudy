# 【问题描述】从键盘输入两个整数n和m（要求n<m），编程求出由n到m(不包含m)中的整数组合而成的所有不含重复数字的三位数。若n和m的输入不合法或者没有符合条件的三位数则提示输出“illegal input"。

# 【输入形式】输入一行，内容为两个以空格分隔的整数，分别表示n和m。

# 【输出形式】以空格分隔输出所有符合条件的三位数。

# 【样例输入】1 4

# 【样例输出】123 132 213 231 312 321

# 【样例输入】2 4

# 【样例输出】illegal input

# 【样例输入】0 3

# 【样例输出】102 120 201 210

def is_valid_input(n,m):
    return n < m and  0<= n < 10 and 0 <= m < 10
def print_num(start,stop):
    test_bool = False
    for i in range(start,stop):
        for j in range(start,stop):
            for k in range(start,stop):
                if len(set([i,j,k])) == 3 and i != 0:
                    print(i*100 + j*10 + k,end=" ")
                    test_bool = True
    if test_bool == False:
        print("illegal input")

n_input,m_input = map(int,input().split(" "))
if is_valid_input(n_input,m_input) == True:
    print_num(n_input,m_input)
else:
    print("illegal input")