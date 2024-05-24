m,n =  map(int,input().split())
matrix = []
for _ in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)
    
sum_matrix = 0
for i in range(m):
    for j in range(n):
        if i == 0 or i == m-1 or j == 0 or j == n-1:
            sum_matrix += matrix[i][j]
            
print(sum_matrix)