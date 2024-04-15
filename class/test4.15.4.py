# 【问题描述】

# 一英亩土地等于43560平方英尺。请编写一个程序，让用户输入以平方英尺为单位输入一片土地的面积，然后计算并输出这片土地的英亩数。

# 【输入形式】

# 从键盘输入土地面积（可以是整数也可以是小数）
# 【输出形式】

# 土地的亩数（小数点后保留3位）
# 【样例输入】

# 1234567
# 【样例输出】

# The land area is 28.342

def land_area(land_s):
    return float(land_s/43560)
land_s = float(input())
print(f"The land area is {land_area(land_s):.3f}")