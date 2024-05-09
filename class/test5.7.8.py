
# 本题要求编写程序输入一个百分制成绩并把其转换为五分制成绩输出。

# 转换规则为：

# 大于等于90分为A； 小于90且大于等于80为B； 小于80且大于等于70为C； 小于70且大于等于60为D； 小于60为E。

# 【输入形式】输入只有一个百分制成绩，如98.5

# 【输出形式】输出对应的五分制成绩，如A

# 【样例输入1】67

# 【样例输出1】D

# 【样例输入2】94.5

# 【样例输出2】A

grade_map = {
    **{i:"A" for i in range(90,101)},
    **{i:"B" for i in range(80,90)},
    **{i:"C" for i in range(70,80)},
    **{i:"D" for i in range(60,70)},
    **{i:"E" for i in range(0,60)}
}

num_input = float(input())
num_input = int(num_input)
result = grade_map.get(num_input)
print(result)