n = 5
for i in range(n):
    ch = chr(ord('E') - i)
    for j in range(i + 1):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
    print()



'''output:
E 
D E 
C D E 
B C D E 
A B C D E'''