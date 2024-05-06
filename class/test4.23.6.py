# 【问题描述】

# 输入一行字符（不能输入中文字符），分别统计出该字符串英文字符、空格、数字和其他字符的个数

# 【输入形式】

# 字符串

# 【输出形式】

# 英文字符个数 空格个数 数字字符个数 其他字符个数

# 【样例输入】

# abcd 1 2 3 4!@#$$%^

# 【样例输出】

# 4 4 4 7

string = input()
letters = 0
spaces = 0
digits = 0
others = 0
for char in string:
    if char.isalpha():
        letters += 1
    elif char.isspace():
        spaces += 1
    elif char.isdigit():
        digits += 1
    else:
        others += 1
print(f'{letters} {spaces} {digits} {others}')