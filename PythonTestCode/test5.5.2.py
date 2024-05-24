
# 【问题描述】

# 输入一个列表，删除其中的重复值，再输出。

# 要求：假设列表中存在k个值为a的元素，删除前k-1个元素，保留最后一个。 不同元素在列表中的相对位置不应被改变。


# 【输入形式】

# [元素1， 元素2, ... , 元素n]


# 【输出形式】

# [元素1，元素2, ... , 元素k]


# 【样例输入】

# [4,3,2,3,2,4,True]
# 【样例输出】

# [3, 2, 4, True]

def create_new_list(list_):
    result = []
    test = set()
    for elem in list_[::-1]:
        if elem not in test:
            test.add(elem)
            result.insert(0,elem)
    return result

list_test = list(input()[1:-1].split(","))
final = create_new_list(list_test)
print("["+', '.join(final)+']')