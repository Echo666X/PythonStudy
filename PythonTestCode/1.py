def calculate_time_to_clear_queue(m, n):
    x = (n - m) * 8  # 初始排队游客份数
    y = x / m  # 每分钟新到游客份数
    z = x / 10  # 10口同开需C分钟清零待检票游客
    return round(x, 1), round(y, 1), round(z, 1)

# 从标准输入读取m和n的值
m = int(input())
n = int(input())

# 计算并输出结果
A, B, C = calculate_time_to_clear_queue(m, n)
print(f"原有排队游客份数:{A}, 每分钟新到游客份数:{B}, 10口同开需{C}分钟清零待检票游客.")
