'''Pattern 2
     A
    A B A
  A B C B A
A B C D C B A


'''


rows = 4
for i in range(1, rows+1):
    print("  "*(rows-i), end="")
    for j in range(i):
        print(chr(65+j), end=" ")
    for j in range(i-2, -1, -1):
        print(chr(65+j), end=" ")
    print()