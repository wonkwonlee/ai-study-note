"""
Adventurer Groups

Input 1: N number of adventurers
Input 2: Panic score for each adventurer
Output: Maximum number of adventurer groups
"""

# Number of adventurers
n = int(input())
# Array of terror score
arr = list(map(int, input().split()))

arr.sort()

# Total number of groups
result = 0
curr = 0
for i in arr:
    # print(f"i is {arr[i]}, curr is {curr}")
    if curr < i:
        curr += 1
        result = max(result, curr)
    else:
        curr = 0

print(result)
