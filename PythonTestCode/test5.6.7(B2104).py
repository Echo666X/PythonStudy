# # 矩阵加法 B2104

# ## 题目描述

# 输入两个 $n$ 行 $m$ 列的矩阵 $A$ 和 $B$，输出它们的和 $A+B$，矩阵加法的规则是两个矩阵中对应位置的值进行加和，具体参照样例。

# ## 输入格式

# 第一行包含两个整数 $n$ 和 $m$，表示矩阵的行数和列数 $(1 \le n \le 100$，$1 \le m \le 100)$。

# 接下来 $n$ 行，每行 $m$ 个整数，表示矩阵 $A$ 的元素。

# 接下来 $n$ 行，每行 $m$ 个整数，表示矩阵 $B$ 的元素。

# 相邻两个整数之间用单个空格隔开，每个元素均在 $1 \sim 1000$ 之间。

# ## 输出格式

# $n$ 行，每行 $m$ 个整数，表示矩阵加法的结果。相邻两个整数之间用单个空格隔开。

# ## 样例 #1

# ### 样例输入 #1

# ```
# 3 3
# 1 2 3
# 1 2 3
# 1 2 3
# 1 2 3
# 4 5 6
# 7 8 9
# ```

# ### 样例输出 #1

# ```
# 2 4 6
# 5 7 9
# 8 10 12
# ```

n,m = map(int,input().split())
matrix_1 = [list(map(int,input().split())) for _ in range(n)]
matrix_2 = [list(map(int,input().split())) for _ in range(n)]
matrix_final = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix_final[i][j] = matrix_1[i][j] + matrix_2[i][j]
for row in matrix_final:
    print(' '.join(map(str,row)))