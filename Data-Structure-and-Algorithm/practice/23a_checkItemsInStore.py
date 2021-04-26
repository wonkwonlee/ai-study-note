"""
Check Items in Store
Binary Search using iteration

5
8 3 7 9 2
3
5 7 9
>> No Yes Yes
"""

# Input data
n = int(input())
store = list(map(int, input().split()))
m = int(input())
cust = list(map(int, input().split()))

# Test case
# n = 5
# store = [8,3,7,9,2]
# m = 3
# cust = [5,7,9]

# Store result
result = []
# Sort items in store
store.sort()


# Binary Search using iteration
def binary_search(start, end, array, target):
    # While loop for start <= end
    while start <= end:
        mid = (start + end) // 2
        # If current value is same as the target, return the current index
        if array[mid] == target:
            return mid
        # If current value is larger, decrease the end index
        elif array[mid] > target:
            end = mid - 1
        # If current value is smaller, increase the start index
        else:
            start = mid + 1
    return None


# Binary search each item in store
for item in cust:
    result.append(binary_search(0, n - 1, store, item))

# Print output
for i in result:
    if i is None:
        print("No", end=' ')
    else:
        print("Yes", end=' ')
