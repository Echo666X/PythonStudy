
n,m = map(int,input().split())
matrix =[list(map(int,input().split())) for _ in range(n)]

matrix_test = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i != 0 and i != n-1 and j != 0 and j != m-1:
            matrix_test[i][j] = round((matrix[i][j]/5 + matrix[i+1][j]/5+matrix[i-1][j]/5+matrix[i][j-1]/5+matrix[i][j+1]/5))
        else:
            matrix_test[i][j] = matrix[i][j]
for row in matrix_test:
    print(*row)