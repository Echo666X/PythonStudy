
# 【问题描述】一球从 h 米高度自由落下， 每次落地后反跳回原高度的 0.5倍； 再落下， 求它在第 N 次落地时， 共经过多少米？  
# 【输入形式】第一行输入高度，第二行输入N

# 【输出形式】输出两位数的浮点数
# 【样例输入】

# 10

# 6
# 【样例输出】

# 29.38

def height(n,h):
    s = h
    for _ in range(n-1):
        h *= 0.5
        s += h*2
    result = float(s)
    print(f'{result:.2f}')
    
height_input = int(input())
number_input = int(input())

height(number_input,height_input)