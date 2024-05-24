# 【问题描述】编写程序，从键盘输入一个数n，输出n以内的所有的回文素数。若n输入不合法（为小数或者负数），则输出提示：“illegal input”。

# 回文素数是指一个数既是素数又是回文数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数称之为素数。例如131既是素数又是回文数。

# 【输入形式】输入一个整数n（n>1）。

# 【输出形式】以空格分隔输出n以内的所有的回文素数。若n输入不合法（为小数或负数），则输出提示“illegal input”

# 【样例输入1】200

# 【样例输出1】2 3 5 7 11 101 131 151 181 191

# 【样例输入2】-4

# 【样例输出2】illegal input

def is_palindrome (num_1):
    return str(num_1) == str(num_1)[::-1]

def is_noun_prime (num_2):
    test_is = True
    for j in range(2,num_2):
        if num_2 % j == 0:
            test_is = False
            break
    return test_is

def is_illegal (num_3):
    try:
        n = int(num_3)
        return n > 1
    except ValueError:
        return False
    
number_input = input()
if is_illegal(number_input) == True:
    number_use = int(number_input)
    for i in range(2,number_use+1):
        if is_palindrome(i) == True and is_noun_prime(i) == True:
            print(i,end=" ")
elif is_illegal(number_input) == False:
    print('illegal input')
