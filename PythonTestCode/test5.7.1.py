# 【问题描述】加密数据。从键盘输入一段数字， 加密规则如下：对于每一个位置上的数字进行如下处理： 每位数字加上 5， 然后除以 10 得到的余数代替该数字， 再将第一位和最后一位交换，第二位与倒数第二位交换， 依此类推， 最后输出加密后的数字密码 。
# 【输入形式】输入一行数字
# 【输出形式】输出加密后的结果
# 【样例输入】

# 123
# 【样例输出】

# 876

# 【样例输入】

# 321
# 【样例输出】

# 678

def encry(num):
    str_num = str(num)
    encry_1 = [(int(digit) + 5)%10 for digit in str_num]
    for i in range(len(encry_1) // 2):
        encry_1[i],encry_1[-i-1] = encry_1[-i-1],encry_1[i]
    encry_2 = ''.join(map(str,encry_1))
    print(encry_2)
    
number = input()
encry(number)