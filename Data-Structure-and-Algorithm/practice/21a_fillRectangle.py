"""
Fill the Rectangle

Input: N width length
Output: Number of different ways to fill in rectangle (Remainder of 796796)
"""

# Width length
n = int(input())

# DP array to store result
dp = [0] * (n+1)


# First and second dp value a_(i-1), a_(i-2)
dp[1] = 1
dp[2] = 3

# a_i = a_(i-1) + 2*a_(i-2)
for i in range(3, n+1):
    # Return the remainder of 796796 to reduce oversize output
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 796796

# print(dp)
# Print output
print(dp[n])
