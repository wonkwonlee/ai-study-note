"""
Loot Maximum Food
Given N number of food storages, each stored with K food, return the maximum 
food available. 
If you loot one food storage, you cannot loot any neighboring storages (i+1, i-1)

Input:   N number of food storages
         K food stored in each storage
         
Output:  Maximum food available


# Example
4
1 3 1 5
>> 8

10
1 3 7 12 8 4 9 10 4 3
>>32
"""
# Number of food storage
n = int(input())
# Food stored in each storage
food = list(map(int, input().split()))

if n != len(food):
    print("Invalid input. Please try again")

# Initialize memoization list
dp = [0] * (n + 1)

# Fill dp list with input food number
for x in range(n):
    dp[x + 1], food[x] = food[x], dp[x + 1]

# First and second value stores
# dp[1] = food[0]
# dp[2] = food[1]

# For-loop from third to n-th
for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])
    print(f"Index is {i} and maximum food is {dp[i]}")

# Print output
print(dp[n])
