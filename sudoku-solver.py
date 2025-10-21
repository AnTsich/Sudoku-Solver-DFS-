import numpy as np 


def nom(x, A, i,j ):
    k = (i//3)*3
    l = (j//3)*3
    S = A[k:k+3,l:l+3]
    if x in A[i,:]:
        return False
    elif x in A[:,j]:
        return False 
    elif x in S:
        return False
    else : 
        return True 
    
    
def dfs(A):
    if 0 not in A:
        return A
    for i in range(9):
        for j in range(9):
            if A[i,j]==0:
                for x in range(1,10):
                    if nom(x,A,i,j) ==True:
                        A[i,j]= x
                        y = dfs(A)
                        if y is not None:
                            return y
                        else: 
                            A[i,j]=0
                return None
        


print("Enter your Sudoku puzzle (9 lines, 9 numbers each, use 0 for blanks):")

grid = []
for _ in range(9):
    row = list(map(int, input().split()))
    grid.append(row)

A = np.array(grid)

rslt = dfs(A)
print("\nSolved Sudoku:")
print(rslt)