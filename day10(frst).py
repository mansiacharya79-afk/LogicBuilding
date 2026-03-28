'''Pattern 1
A
B B
C C C
D D D D
E E E E E
'''


ch = 65   
for i in range(1,6):
    for j in range(i):
        print(chr(ch), end=" ")
    print()
    ch += 1