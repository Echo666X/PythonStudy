matrix = [] #创建空矩阵
for _ in range(5): #按行读取
    row = list(map(int,input().split()))
    matrix.append(row)
    
saddle_point = [] #鞍点初始化
for i in range(5):
    for j in range(5):
        test_value = matrix[i][j]
        max_in_row = max(matrix[i])
        min_in_col = min(matrix[k][j] for k in range(5))
        if test_value == max_in_row and test_value == min_in_col:
            saddle_point.append((i+1,j+1,test_value))
            
if saddle_point != []:
    i,j,test_value = saddle_point[0]
    print(f"{i} {j} {test_value}")
else:
    print('not found')
    