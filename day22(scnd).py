'''Finding the Longest Sequence of Consecutive 1s in a Binary Array
Write a program to find the longest sequence of consecutive 1s in a binary array.
'''
arr = list(map(int, input("Enter binary values: ").split()))
max_count = 0
current_count = 0
for num in arr:
    if num == 1:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0
print("Longest consecutive 1s:", max_count)


'''Output
Enter binary values: 1 1 0 1 1 1 0 1
Longest consecutive 1s: 3

'''