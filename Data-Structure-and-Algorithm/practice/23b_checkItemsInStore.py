"""
Check Items in Store
# Counting Sort

5
8 3 7 9 2
3
5 7 9
>> No Yes Yes
"""
n = int(input())
store = list(map(int, input().split()))
m = int(input())
cust = list(map(int, input().split()))
# n = 5
# store = [8,3,7,9,2]
# m = 3
# cust = [5,7,9]

result = [0] * 1000001

for item in store:
    result[item] = 1

for i in cust:
    if result[i] == 1:
        print("Yes", end=' ')
    else:
        print("No", end=' ')
