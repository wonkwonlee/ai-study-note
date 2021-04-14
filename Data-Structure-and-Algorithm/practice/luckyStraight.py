"""
Lucky Straight

Input: Player's score N. The digit of N is always even number.
Output: Print LUCKY if "Lucky Straight" is available and READY if not.
"""


# My Code
N = input()

half = len(N) // 2
left, right = 0, 0
for i in range(half):
    left += int(N[i])
    right += int(N[i + half])

if left == right:
    print("LUCKY")
else:
    print("READY")


# Example
n = input()

summary = 0
length = len(n)

for i in range(length // 2): 
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')
else:
    print("READY")
