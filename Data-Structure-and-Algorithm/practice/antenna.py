"""
Antenna
Given N number of houses, an antenna will be set up on a location
Return the position that minimizes the sum of distances.
"""

n = int(input())
house = list(map(int, input().split()))
house.sort()
# print(house)
print(house[(n-1) // 2])
