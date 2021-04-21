"""
Sequential Search
"""


def sequential_search(target, array):
    # From 0 to length of array
    for i in range(len(array)):
        # Return index + 1 if value is the target value
        if array[i] == target:
            return i + 1


arr = [1, 2, 41, 12, 43, 36, 54, 67, 100, 99]
nums = 3
find = [100, 99, 0]

for i in range(nums):
    loc = sequential_search(find[i], arr)
    if loc is None:
        print(f"The target value {find[i]} is not in the array.")
    else:
        print(f"The target value {find[i]} is located at the {loc}.")
