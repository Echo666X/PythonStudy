# 开车超速是要罚款的，某国相应法律如下：

# 情况	处罚
# 车速 ≤ 限速	程序输出：未超速
# 超速比 ≤ 10%	程序输出：超速警告
# 10% <超速比≤ 20%	程序输出：罚款100元
# 20% <超速比≤ 50%	程序输出：罚款500元
# 50% <超速比≤ 100%	程序输出：罚款1000元
# 超速比 > 100%	程序输出：罚款2000元
# 请编写程序，程序从输入的第1行读取车速（整数），从输入的第2行读取限速值（整数），然后使用条件分支语句进行判断，输出如表所示的处罚结论。
def speeding_penalty(speed, limit):
    # 计算超速比例
    speed_ratio = (speed - limit) / limit * 100

    # 根据超速比例进行判断
    if speed <= limit:
        return "未超速"
    elif speed_ratio <= 10:
        return "超速警告"
    elif speed_ratio <= 20:
        return "罚款100元"
    elif speed_ratio <= 50:
        return "罚款500元"
    elif speed_ratio <= 100:
        return "罚款1000元"
    else:
        return "罚款2000元"

# 从输入中读取车速和限速值
speed = int(input().strip())
limit = int(input().strip())

# 输出处罚结论
print(speeding_penalty(speed, limit))
