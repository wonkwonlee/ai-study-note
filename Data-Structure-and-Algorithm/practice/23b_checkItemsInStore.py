"""
Check Items in Store
Counting Sort

5
8 3 7 9 2
3
5 7 9
>> No Yes Yes
"""

# Input data
n = int(input())
store = list(map(int, input().split()))
m = int(input())
cust = list(map(int, input().split()))

# Test case
# n = 5
# store = [8,3,7,9,2]
# m = 3
# cust = [5,7,9]

# Initialize result array
result = [0] * 1000001

# Mark existing items in store as 1
for item in store:
    result[item] = 1

# Check if customer requested items exist in result array
for i in cust:
    # If item exists, print yes
    if result[i] == 1:
        print("Yes", end=' ')
    # If item does not exist, print no
    else:
        print("No", end=' ')
