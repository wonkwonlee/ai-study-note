"""
Three in Time

Input: N hour
Output: Number of time that contains 3

# Example
5
>> 11475
"""


# Input hour
n = int(input())

count = 0
# Hour from 0 to h
for h in range(n + 1):
    # Minute from 0 to 59
    for m in range(60):
        # Second from 0 to 59
        for s in range(60):
            # Time in string from 0 00 00 ~ h 59 59
            time = str(h) + str(m) + str(s)
            if '3' in time:
                count += 1

print(count)
