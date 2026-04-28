'''Matrix Transpose
Transpose of a matrix is obtained by swapping its rows with columns.'''


A = [[1, 2, 3],
     [4, 5, 6]]

for j in range(3):
    for i in range(2):
        print(A[i][j], end=" ")
    print()


'''output
1 4
2 5
3 6
'''