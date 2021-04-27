"""
Bowling Ball Weight
Return possible number combinations of two bowling balls.

Input1: N number of bowling balls, M maximum weight of a bowling ball
Input2: Weight of each bowling ball
Output: Maximum number of possible combinations

# Example
5 3
1 3 2 3 2
>> 8 (1,2) (1,3) (1,4) (1,5) (2,3) (2,5), (3,4) (4,5)
"""

from itertools import combinations

n, m = map(int, input().split())  # 5, 3
balls = list(map(int, input().split()))  # [1,3,2,3,2]
result = 0

# Count the number of combinations
for a, b in combinations(balls, 2):
    if a != b:
        result += 1

print(result)
