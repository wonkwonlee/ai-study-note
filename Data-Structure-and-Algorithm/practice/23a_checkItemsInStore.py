"""
Check Items in Store
# Binary Search

5
8 3 7 9 2
3
5 7 9
>> No Yes Yes
"""
n = int(input())
store = list(map(int, input().split()))
m = int(input())
cust = list(map(int, input().split()))
# n = 5
# store = [8,3,7,9,2]
# m = 3
# cust = [5,7,9]

result = []

store.sort()


def binary_search(start, end, array, target):
    mid = (start + end) // 2
    if start > end:
        return None
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(start, mid - 1, array, target)
    else:
        return binary_search(mid + 1, end, array, target)


for item in cust:
    result.append(binary_search(0, n - 1, store, item))

for i in result:
    if i is None:
        print("No", end=' ')
    else:
        print("Yes", end=' ')
