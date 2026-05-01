'''Write a Python program to add two matrices.'''

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)
print(result)

'''output
[[6, 8], [10, 12]]'''