n, m = map(int, input.split())

nums = []
for i in range(n):
    nums.append(int(input()))

mx, mn = max(nums), 0
result = []

while True:
    height = (mx + mn) // 2
    for x in nums:
        result.append(max(x - height, 0))

    if sum(result) > 6:
        mn = height + 1

    elif sum(result) < 6: 
        mx -= 1
    else:
        break