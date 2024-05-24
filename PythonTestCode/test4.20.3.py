# 【问题描述】

# 以下是一段温度转换程序，可以实现华氏温度和摄氏温度的转换，请自行阅读程序，在理解程序的基础上，仿照此程序，写一个人民币和美元之间的货币转换程序。



# 该程序实现以下功能：

# 示例：输入212F      输出100.00C

#      输入100c      输出212.00F

#       输入不符合格式要求，输出“Error”     



# TempStr = input()

# if TempStr[-1] in ['F','f']:

#     C = (eval(TempStr[0:-1]) - 32)/1.8

#     print("%.2fC"%(C))

# elif TempStr[-1] in ['C','c']:

#     F = 1.8*eval(TempStr[0:-1]) + 32

#     print("%.2fF"%(F))

# else:

#     print("Error")



# 人民币和美元是世界上通用的两种货币之一，写一个程序进行货币间币值转换，其中：人民币和美元间汇率固定为：1美元 = 6.78人民币。

# 程序可以接受人民币或美元输入，转换为美元或人民币输出。人民币采用&符号或RMB表示，美元采用$或USD表示，符号和数值之间没有空格。

# 注意：人民币和美元间符号在转换中要对等，&和$相互对应，RMB和USD相互对应。





# 【输入形式】

# 美元或人民币

# 【输出形式】

# 转换后的人民币或美元，保留两位小数

# 输入不符合格式要求，输出“Error”

# 【样例输入1】

# $128.00

# 【样例输出1】

# &867.84

# 【样例输入2】

# &12.9

# 【样例输出2】

# $1.90

# 【样例输入3】

# RMB123

# 【样例输出3】

# USD18.14

# 【样例输入4】

# USD18.14

# 【样例输出4】

# RMB122.99

money = input()

if money[0] in ['&']:
    
    USD = float(money[1:])/6.78

    print(f"${USD:.2f}")
    
elif money[:3] in ['RMB']:
    
    USD = float(money[3:])/6.78
    
    print(f"USD{USD:.2f}")
    
elif money[0] in ['$']:

    RMB = float(money[1:])*6.78

    print(f"&{RMB:.2f}")

elif money[:3] in ['USD']:
    
    RMB = float(money[3:])*6.78
    
    print(f"RMB{RMB:.2f}")

else:

    print("Error")
    
# 字符串切片：从一个字符串中提取新的内容组成新的字符串
# the basical syntax of it is as follows:
# string[start:stop:step]
# start: 切片的起始位置，包含该字符，默认为0
# stop：切片的结束位置，不包含该字符，默认为字符串长度
# step：切片步长，默认为1，表示每次移动一个字符