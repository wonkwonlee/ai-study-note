"""
Check Items In Store

Binary Search
"""


def find_items(target, array, start, end):
    # If start > end, that means all elements are visited
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return find_items(target, array, start, mid - 1)
    else:
        return find_items(target, array, mid + 1, end)


# N is number of items at the store
n = int(input())

# Store data into store_items list
store_items = list(map(int, input().split()))

# M is the number of items customer request
m = int(input())

# Store data into request_items list
request_items = list(map(int, input().split()))

# Sort store_items list
store_items.sort()
for x in request_items:
    result = find_items(x, store_items, 0, n - 1)
    if result is None:
        print("No")
    else:
        print("Yes")
