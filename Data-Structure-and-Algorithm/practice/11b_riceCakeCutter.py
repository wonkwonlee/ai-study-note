"""
Rice Cake Cutter

# Binary Search
"""


def height_search(array, nums, target, start, end):
    # Binary search middle index
    mid = (start + end) // 2
    # If there is no optimal point, return current rice cake height
    if start > end:
        return mid
    # Temporary var
    curr_height = 0
    # Sum of current rice cake
    for x in array:
        curr_height += max(x - nums[mid], 0)
    # Binary search
    if curr_height == target:
        return mid
    elif curr_height > target:
        return height_search(array, nums, target, mid + 1, end)
    else:
        return height_search(array, nums, target, start, mid - 1)


# N is number of rice cakes, M is the requested height of rice cake
n, m = map(int, input().split())
# Store the height of each rice cake
rice_cake = list(map(int, input().split()))

# Initialize a list to store height from 0 to max value
heights = [x for x in range(max(rice_cake) + 1)]
# Find the target height
target_height = height_search(rice_cake, heights, m, min(heights), max(heights))

print(target_height)


# # Example 1: Binary Search
# n, m = list(map(int, input().split(' ')))
# array = list(map(int, input().split()))
#
# start = 0
# end = max(array)
# result = 0
#
# # Binary search until start > end
# while start <= end:
#     # Sum of customer's rice cakes
#     total = 0
#     mid = (start + end) // 2
#     for x in array:
#         if x > mid:
#             total += x - mid
#     # Binary search algorithm
#     if total < m:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1
#
# print(result)
