"""
Binary Search

Use binary search to find target element in the array.
"""

# N number of elements and the target value
n, target = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = len(array) - 1


# Binary search using recursion
def binary_search(start, end, target):
    mid = (start + end) // 2
    if start > end:
        return None
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(start, mid - 1, target)
    else:
        return binary_search(mid + 1, end, target)


result = binary_search(start, end, target)

if result is None:
    print("The target element does not exist.")
else:
    print(result + 1)
