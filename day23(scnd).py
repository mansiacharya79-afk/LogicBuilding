'''Find the Majority Element in an Array
Find the element that appears more than n/2 times in the array (if any)
'''


arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
n= len (arr)
for num in arr:
    if arr.count(num)> n//2:
        print("Majority Element:", num)
        break
else:
        print("No Majority Element")
        

'''Output
Majority Element: 4
'''