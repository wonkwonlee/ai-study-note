"""
Addition and Multiplication
Multiply if number is other than 0 and 1.
Add if number is 0 or 1.
Return the largest output .
"""

s = input()

result = int(s[0])

for i in range(1, len(s)):
    if int(s[i]) <= 1 or result <= 1:
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)
