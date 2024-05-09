# # 最高的分数

# ## 题目描述

# 孙老师讲授的《计算概论》这门课期中考试刚刚结束，他想知道考试中取得的最高分数。因为人数比较多，他觉得这件事情交给计算机来做比较方便。你能帮孙老师解决这个问题吗？

# ## 输入格式

# 输入两行，第一行为整数 $n$（$1 \le n<100$），表示参加这次考试的人数。第二行是这 $n$ 个学生的成绩，相邻两个数之间用单个空格隔开。所有成绩均为 $0$ 到 $100$ 之间的整数。

# ## 输出格式

# 输出一个整数，即最高的成绩。

# ## 样例 #1

# ### 样例输入 #1

# ```
# 5
# 85 78 90 99 60
# ```

# ### 样例输出 #1

# ```
# 99
# ```

def find_high(grades):
    result = max(grade for grade in grades)
    return result

number = int(input())
grades_list = list(map(int,input().split(" ")))

result_output = find_high(grades_list)
print(result_output)
    