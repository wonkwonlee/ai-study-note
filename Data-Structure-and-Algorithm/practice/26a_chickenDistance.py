"""
Minimum Chicken Distance

# Example
5 3
00100
00201
01200
00100
00002
>> 5
"""

# N number of houses and M number of chicken stores
n, m = map(int, input().split())
graph = []

# [[0,0,1,0,0],[0,0,2,0,1],[0,1,2,0,0],[0,0,1,0,0],[0,0,0,0,2]]
for _ in range(n):
    graph.append(list(map(int, input())))

# print(graph)

# Moving directions
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Arrays to store coordinates of chicken stores and customer houses
stores = []
houses = []


# Find chicken distance using BFS algorithm
def chicken_distance():
    x, y = 1, 1

    q = [(x, y)]
    while q:
        for i in range(4):
            # Next x and y coordinate
            nx = x + dx[i]
            ny = y + dy[i]

            # Out of boundary
            if nx < 0 or nx >= n or ny < 1 or ny >= n:
                continue
            else:
                # Check if current coordinate is a chicken store
                if graph[nx][ny] == 2:
                    # Store current location to stores array
                    stores.append((nx, ny))
                    q.append((nx, ny))
                    q.pop(0)
                # Check if current coordinate is a customer house
                elif graph[nx][ny] == 1:
                    # Store current location to houses array
                    houses.append((nx, ny))
                    q.append((nx, ny))
                    q.pop(0)
                # Check if current coordinate is empty
                else:
                    continue

            x, y = nx, ny

    return find_min_distance(houses, stores)


# Function to get minimum distance
def find_min_distance(arr1, arr2):
    min_dist = []
    mn = 2 * 31 - 1
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            # Calculate current chicken distance by manhattan distance
            dist = abs(arr2[j][0] - arr1[i][0]) + abs(arr2[j][1] - arr1[i][1])
            # Update new minimum distance
            if dist < mn:
                min_dist[i] = dist
                mn = dist

    return sum(min_dist)


print(chicken_distance())
