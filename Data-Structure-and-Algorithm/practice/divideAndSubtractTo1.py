"""
Divide and subtract to 1
Given integer x, there are four operations available.
    1. If x is divisible by 5, divide it by 5.
    2. If x is divisible by 5, divide it by 5.
    3. If x is divisible by 5, divide it by 5.
    4. Subtract 1 from x.
Find the minimum operations to return output.

# Example
26 
>> 3 (26 - 1, 25 / 5, 5 / 5)
"""


# Input integer x
x = int(input())

# Initialize memoization list
dp = [0] * 30000

# Integer 1 does not need any operation
dp[1] = 0

for i in range(2, x + 1):
    # Subtract 1
    dp[i] = 1 + dp[i - 1]   
    # Divide operations
    # Compare the current minimum with value after division 
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[int(i / 5)] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[int(i / 3)] + 1)    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[int(i / 2)] + 1)
    print(f"i is {i}, and value is {dp[i]}")

# Print output
print(dp[x])
