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

season_dict = {
    **{i: "spring" for i in range(3,6)},
    **{i: "summer" for i in range(6,9)},
    **{i: "autumn" for i in range(9,12)},
    **{i: "winter" for i in {12,1,2}}
}

month = int(input())
season = season_dict.get(month,'error')
print(season)