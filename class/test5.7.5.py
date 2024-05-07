# 【问题描述】从键盘不断地输入整数，当输入“#”时程序退出，然后打印出所输入整数的个数和总和。

# 【输入形式】输入多行，每行从键盘输入一个数，直到输入#为止，则输入停止。

# 【输出形式】输出一行，内容为以空格分隔的两个数，分别表示输入整数的个数n和这些整数的总和s。

# 【样例输入】1

#                     2

#                     #

# 【样例输出】2 3

count = 0
total = 0
command_input = ''
while command_input != '#':
    command_input = input()
    if command_input == '#':
        break
    count += 1
    total += int(command_input)
    
print(count,total)