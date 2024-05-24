
def matrix_spin(row,column,matrix):
    '''enter a n lines m column balck and white image,
    rotate it clockwise 90 output after 90 degrees'''
    matrix_spined = [[0]*row for _ in range(column)]
    for i in range(row):
        for j in range(column):
            matrix_spined[j][row -1 - i] = matrix[i][j]
    return matrix_spined

n,m = map(int,input().split())
matrix_input = [list(map(int,input().split())) for _ in range(n)]
matrix_spin_test = matrix_spin(n,m,matrix_input)

for row in matrix_spin_test:
    print(*row)