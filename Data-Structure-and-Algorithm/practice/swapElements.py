"""
Swap Elements
Given two arrays A, B with length of N, swap maximum values of array A with
minimum values of array B at most K times operations.
Return the maximum sum of elements in the array A.

Example
N = 5, K = 3
A = [1,2,5,4,3]
B = [5,5,6,6,5]
>> 26 (A = [6,6,5,4,5] after swap operations)
"""

# N is the length of arrays, K is the maximum swap operations
N, K = map(int, input().split())

# First array
array_A = list(map(int, input().split()))   # [1,2,5,4,3]
array_A.sort()                              # [1,2,3,4,5]
# Second array
array_B = list(map(int, input().split()))   # [5,5,6,6,5]
array_B.sort()                              # [5,5,5,6,6]

# From i=0 to K-1
for i in range(K):
    # Swap min values in array_A with max values in array_B
    array_A[i], array_B[-i-1] = array_B[-i-1], array_A[i]

# Check array_A and array_B after swap operations
# print(array_A)                            # [6,6,5,4,5]
# print(array_B)                            # [5,5,3,2,1]

# Sum of array_A
result = sum(array_A)
print(result)
