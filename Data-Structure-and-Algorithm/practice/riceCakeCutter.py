n, m = map(int, input().split())

nums = []
for i in range(n):
    input_data = int(input().split())
    nums.append(input_data)

mx, mn = max(nums), 0
result = []

while sum(result) == m:
    height = (mx + mn) // 2
    for x in nums:
        result.append(max(x - height, 0))

    if sum(result) > m:
        mn = height + 1

    elif sum(result) < m: 
        mx -= 1

print(height)