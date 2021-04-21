"""
Zero and One

# Example
Input: 0001100
Output: 1

Input: 01010
Output: 2
"""


# String input
s = input()
# count0 is 0s to 1s, and count1 is 1s to 0s
count0, count1 = 0, 0

# Check the first element in the string
if s[0] == '0':
    count0 += 1
else:
    count1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        # If next element is 0, increase count0
        if s[i + 1] == '0':
            count0 += 1
        # If next element is 1, increase count1
        else:
            count1 += 1

print(min(count0, count1))
