n = 5
space = 0

for i in range(n, 0, -1):
    print(" " * space + "* " * (2*i - 1))
    space += 2