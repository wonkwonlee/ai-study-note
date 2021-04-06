"""
Quick Sort in Reverse

list.sort() : Affect the original. Return None.
sorted(list) : Do not affect the original. Return a new list.

# Quick Sort
"""


def quick_reverse(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x > pivot]
    right = [x for x in tail if x <= pivot]

    return quick_reverse(left) + [pivot] + quick_reverse(right)


num = []
n = int(input())

for i in range(n):
    num.append(int(input()))

for i in quick_reverse(num):
    print(i, end=" ")
