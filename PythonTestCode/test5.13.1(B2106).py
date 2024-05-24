def transpose(mat,N,M):
    tran_mat = [[0]*N for _ in range(M)]
    for i in range(N):
        for j in range(M):
                tran_mat[j][i] = mat[i][j]
    return tran_mat

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range (n)] 

matrix_transposed = transpose(matrix,n,m)
for row in matrix_transposed:
    print(*row)
# the * is used to unpack the list