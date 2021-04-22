"""
Greedy Coin
"""
# My Code
n = 1260

count = 0
while n > 0:
    if n // 500:
        count += n // 500
        n %= 500
    if n // 100:
        count += n // 100
        n %= 100
    if n // 50:
        count += n // 50
        n %= 50
    if n // 10:
        count += n // 10
        n %= 10

print(count)

# Example Code
coins = [500, 100, 50, 10]
n = 1260
count = 0

for i in coins:
    count += n // i
    n %= i

print(count)
