n_input = int(input())
matrix = [list(map(int,input().split(' '))) for _ in range(n_input)]
def gold(list_,n):
    total_gold = 0
    for i in range(n):
        total_gold += list_[i][0]
    return total_gold
    
def silver(list_,n):
    total_silver = 0
    for j in range(n):
        total_silver += list_[j][1]
    return total_silver
        
def bronze(list_,n):
    total_bronze = 0
    for k in range(n):
        total_bronze += list_[k][2]
    return total_bronze

total_medal = gold(matrix,n_input)+silver(matrix,n_input)+bronze(matrix,n_input)
print(f"{gold(matrix,n_input)} {silver(matrix,n_input)} {bronze(matrix,n_input)} {total_medal}")