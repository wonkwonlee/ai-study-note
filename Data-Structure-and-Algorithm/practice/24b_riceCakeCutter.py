"""
Rice Cake Cutter

# Binary Search
"""

n, m = map(int, input().split())    # 4, 6
heights = list(map(int, input().split()))   # heights = 19, 15, 10, 17

result = 0

start, end = 0, max(heights)
while start <= end:
    curr = 0
    mid = (start + end) // 2
    for i in heights:
        curr += max(i - mid, 0)

    if curr < m:
        end = mid - 1
    elif curr > m:
        start = mid + 1
    else:
        result = mid
        break

print(result)
