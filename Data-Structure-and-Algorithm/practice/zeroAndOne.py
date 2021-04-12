"""
Zero and One

# Example
Input: 0001100
Output: 1

Input: 01010
Output: 2
"""

s = str(input())

count = 0
result = 0

# From 0 to 1
for i in range(len(s)):
    if s[i] == 0:
        
