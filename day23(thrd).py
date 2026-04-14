'''Reverse an Array
Reverse the order of elements in the given array.
'''
arr = list(map(int, input("Enter elements: ").split()))
arr = arr[::-1]
print("Reversed Array:", arr)


'''Output
Enter elements: 8 7 9 0 3
Reversed Array: [3, 0, 9, 7, 8]'''