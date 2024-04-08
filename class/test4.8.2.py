def mix_colors(color1, color2):
    # 将输入的颜色名称转换为小写字母
    color1 = color1.lower()
    color2 = color2.lower()

    # 定义原色与次生色的对应关系
    color_map = {
        frozenset({'red', 'blue'}): 'purple',
        frozenset({'red', 'yellow'}): 'orange',
        frozenset({'blue', 'yellow'}): 'green'
    }

    # 如果输入的颜色是相同的或者不是三原色的名称，则输出错误信息
    if color1 == color2 or color1 not in color_map or color2 not in color_map:
        return "error"
    else:
        # 混合得到的次生色
        secondary_color = color_map[frozenset({color1, color2})]
        return secondary_color

# 从输入中读取原色1和原色2
color1 = input().strip()
color2 = input().strip()

# 输出混合得到的次生色或错误信息
print(mix_colors(color1, color2))
