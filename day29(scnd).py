'''Search an Element in a Matrix
Search for a given element in a matrix and return its position.
'''
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
target = 9
for i in range(3):
    for j in range(3):
        if A[i][j] == target:
            print("Found at:", (i, j))

'''output
Found at: (2, 2)
'''