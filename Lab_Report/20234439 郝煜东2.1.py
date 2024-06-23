from datetime import datetime

def read_card_info(file_path):
    """读取刷卡信息"""
    card_data = {}
    with open(file_path, 'r', encoding='utf-8') as file:  # 以只读模式打开文件，并指定编码
        for line in file:
            name, time_str = line.strip().split(',')
            if name not in card_data:
                card_data[name] = []
            card_data[name].append(time_str)
    return card_data

def calculate_total_duration(card_data):
    """计算每位同学的锻炼总时长"""
    durations = {}
    for name, times in card_data.items():
        times.sort()  # 按时间排序
        total_seconds = 0
        for i in range(0, len(times), 2):
            if i + 1 < len(times):
                start_time = datetime.strptime(times[i], "%H:%M:%S")
                end_time = datetime.strptime(times[i+1], "%H:%M:%S")
                total_seconds += int((end_time - start_time).total_seconds())
        durations[name] = total_seconds
    return durations

def write_sorted_durations(durations, output_path):
    """将计算结果按要求排序并写入文件"""
    # 按锻炼时长降序排序，如锻炼时长相同，则按姓名降序
    sorted_durations = sorted(durations.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    with open(output_path, 'w', encoding='utf-8') as file:  # 以写入模式打开文件，并指定编码
        for name, duration in sorted_durations:
            file.write(f"{name},{duration}\n")

# 主程序
card_info = read_card_info('in1.txt')
total_durations = calculate_total_duration(card_info)
write_sorted_durations(total_durations, 'out1.txt')
