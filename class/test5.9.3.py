# 【问题描述】

# 统计字符串列表中每个字母出现的次数。
# 编写程序，读入一个仅包含字符串对象的列表，然后统计该列表中每个字母出现的次数。 列表中的字符串对象仅包含小写英文字母。


# 【输入形式】

# 一个仅包括字符串对象的列表，且全部字符串对象中仅出现小写英文字母。


# 【输出形式】

# 字母,次数
# ...
# 字母,次数
# (注意按a-z的顺序输出)


# 【样例输入】

# ["aaab", "cccdz"]

# 【样例输出】

# a,3
# b,1
# c,3
# d,1
# z,1
def count_letters(string_list):
    letter_count = {}
    for string in string_list:
        for char in string:
            if char.isalpha():
                letter_count[char] = letter_count.get(char, 0) + 1
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[0])
    for letter, count in sorted_letters:
        print(f"{letter},{count}")

def main():
    input_string = input()
    string_list = list(input_string)
    count_letters(string_list)

main()
