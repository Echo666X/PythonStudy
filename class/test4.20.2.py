# 【问题描述】

# 根据用户输入的月份，打印该月份所属的季节，如果输入的数据不在1~12范围内，输出“error" 

# 提示：3，4，5 spring ；6，7，8 summer ；9，10，11 autumn ；12，1，2 winter

# 【输入形式】

# 月份（整数）
# 【输出形式】

# spring or summer or autumn or winter or error

# 【样例输入】
# 3

# 【样例输出】
# spring

def season(n):
    if n == 3 or n == 4 or n == 5:
        print("spring")
    elif n == 6 or n == 7 or n == 8:
        print("summer")
    elif n == 9 or n == 10 or n == 11:
        print("autumn")
    elif n ==12 or n == 1 or n == 2:
        print("winter")
    else:
        print("error")
        
season(int(input()))

    