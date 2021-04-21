"""
Fixed Value
"""


# Binary Search using recursion
def binary_search(array, start, end):
    if start > end:
        return None
    # Middle point and target
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)


# N number of elements
n = int(input())
array = list(map(int, input().split()))

# Start = 0, end = n - 1
result = binary_search(array, 0, n - 1)

if result is None:
    print(-1)
else:
    print(result)
