n = 4
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()

'''output:
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
'''