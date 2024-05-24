# 编写一个程序，请用户输入某班级男生和女生的人数，然后显示该班级的性别比例,结果保留两位小数。

# 【输入形式】

# 男生人数

# 女生人数

# 【输出形式】

# The male students ratio is 【百分比】,the female students ratio is 【百分比】

# 【样例输入1】

# 12

# 8

# 【样例输出1】

# The male students ratio is 60.00%,the female students ratio is 40.00%

# 【样例输入2】

# 8

# 4

# 【样例输出2】

# The male students ratio is 66.67%,the female students ratio is 33.33%

male_number = int(input())
female_number = int(input())
print(f"The male students ratio is {male_number*100/(male_number+female_number):.2f}%,the female students ratio is {female_number*100/(male_number+female_number):.2f}%")