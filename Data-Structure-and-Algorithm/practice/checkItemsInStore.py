"""
Check Items In Store

Binary Search
"""


def binary_search(target, array, start, end):
    # If start > end, that means all elements are visited
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(target, array, start, mid - 1)
    else:
        return binary_search(target, array, mid + 1, end)


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
    result = binary_search(x, store_items, 0, n - 1)
    if result is None:
        print("No")
    else:
        print("Yes")


# # Example 1: Binary Search
# def binary_search(array, target, start, end):
#     # Use while instead of if start > end
#     while start <= end:
#         mid = (start+end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#               end = mid - 1
#         else:
#           start = mid + 1
#     return None
#
# n = int(input())
#
# array = list(map(int, input().split()))
# array.sort()
#
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#   result = binary_search(array, i, 0, n - 1)
#   if result != None:
#     print('yes', end = ' ')
#   else:
#     print('no', end = ' ')


# # Example 2: Counting Sort
# n = int(input())
# # Create an empty array filled with out of boundary value
# array = [0] * 1000001
#
# # Mark items to array as 1
# for i in input().split():
#     array[int(i)] = 1
#
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     if array[i] == 1:
#         print('yes', end = ' ')
#     else:
#         print('no', end = ' ')
