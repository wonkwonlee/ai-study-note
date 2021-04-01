def height_search(array, nums, target, start, end):
    # Binary search middle index
    height = (start + end) // 2
    # If there is no optimal point, return current height value
    if start > end:
        return height
    # Temporary var
    curr_height = 0
    # Sum of current rice cake
    for x in array:
        curr_height += max(x - nums[height], 0)
    # Binary search
    if curr_height == target:
        return height
    elif curr_height > target:
        return height_search(array, nums, target, height + 1, end)
    else:
        return height_search(array, nums, target, start, height - 1)


# N is number of rice cakes, M is the requested height of rice cake
n, m = map(int, input().split())
# Store the height of each rice cake
rice_cake = list(map(int, input().split()))

# Initialize a list to store height from 0 to max value
heights = [x for x in range(max(rice_cake) + 1)]
# Find the
target_height = height_search(rice_cake, heights, m, min(heights), max(heights))

print(target_height)
