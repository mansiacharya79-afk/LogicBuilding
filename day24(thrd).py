'''Move Zeros to the End of an Array
Move all zeros in the array to the end while maintaining the relative order of non-zero elements.
'''


arr = list(map(int, input("Enter elements : ").split()))
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j], arr[i] = arr[i], arr[j]
        j += 1
print("Output:", arr)


'''Output:
Enter elements : 0 1 0 3 12
Output: [1, 3, 12, 0, 0]
'''