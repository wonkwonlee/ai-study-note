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

# N number of balls, M max weight
N, M = map(int, input().split())
# List to store the weight of each ball
balls = list(map(int, input().split()))

# Maximum weight M is between 1 to 10
weight = [0] * 11

# Count the number of balls in each weight
for data in balls:
    weight[data] += 1

result = 0
# Loop from weight between 1 to 10
for i in range(1, M + 1):
    # Available combinations: (total ball nums - current weight ball nums)
    N -= weight[i]
    # Add current ball num * available combinations
    result += N * weight[i]

print(result)
