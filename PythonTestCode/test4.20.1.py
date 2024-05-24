# 【问题描述】

# 红色(red)、蓝色(blue)和黄色(yellow)被称为原色(primary color)。 当两种原色混合时，将得到次生色(secondary color)。

# 规则如下： 

# 当红色与蓝色混合时，将得到紫色(purple)。 

# 当红色与黄色混合时，将得到橙色(orange)。 

# 当蓝色与黄色混合时，将得到绿色(green)。 

# 编写一个程序，根据用户输入的欲混合的两种原色，输出混合得到的次生色的名称。 如果用户输入的不是三原色的名称，或者输入的两个颜色相同，则输出“error”

# 【输入形式】

# 原色1

# 原色2
# 【输出形式】

# 次生色 or error
# 【样例输入1】

# red

# blue

# 【样例输出1】

# purple

# 【样例输入2】

# red

# red

# 【样例输出2】

# error
def mix_color(value1,value2):
    """ 计算三原色结果"""
    if value1 == "red" and value2 == "blue" or value2 == "red" and value1 == "blue":
        return "purple"
    elif value1 == "red" and value2 == "yellow" or value1 == "yellow" and value2 == "red":
        return "orange"
    elif value1 == "blue" and value2 == "yellow" or value1 == "yellow" and value2 == "blue":
        return "green"
    elif value2 == value1:
        return "error"
    else:
        return "error"

color1 = input().lower()
color2 = input().lower()
print(mix_color(color1,color2))