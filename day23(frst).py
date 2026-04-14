'''Find the Missing Number in an Array
Given an array of numbers from 1 to n with one number missing, find the missing number.
'''


arr = [1, 2, 4, 5, 6]
n = len(arr) + 1  
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
missing_number = expected_sum - actual_sum
print("Missing Number:", missing_number)


'''Output
Missing Number: 3'''