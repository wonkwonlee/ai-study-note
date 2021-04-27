"""
Dummy Game
Similar to snake game

Input 1: N size of square board [2, 100]
Input 2: K number of apples [0, 100]
Input 3: K lines of apple locations (row, col)
Input 4: L number of turns [1, 100]
Input 5: L lines of turning directions (time, direction)

# Example
6
3 
3 4
2 5
5 3
3 
3 D
15 L
17 D

>> 9
"""

from collections import deque

# N size of square board
# n = int(input())
n = 6
# N x N square board
graph = [[0] * n for _ in range(n)]
# K number of apples
# k = int(input())
k = 3

# Locate apples to coordinates
# for _ in range(k):
#     a, b = map(int, input().split())
#     # Coordinate is 0 if empty, 1 if apple exists, and 2 if snake body exists
#     graph[a-1][b-1] = 1

graph[2][3] = 1
graph[1][4] = 1
graph[4][2] = 1



# print(graph)

# L number of changing directions
# l = int(input())
l = 3

count = 0
directions = []
for _ in range(l):
    x, y = input().split()
    # print(int(x) - count)
    directions.append([int(x) - count, y])
    count = int(x)

# Current moving direction
move_dir = 0

snake.append([0, 0])

# Move directions
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 
graph[0][0] = 2
time = 0

while True:

    nx = x + dx[move_dir]
    ny = y + dy[move_dir]

    # If snake hits the wall or its tail, break the loop
    if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 1:
        time += 1
        break
    else:
        # If (nx, ny) is apple
        if graph[nx][ny] == 1:
            # Increase snake body
            graph[nx][ny] = 2
            snake.append([nx, ny])
        else:
            pass

    # Update current position and increase time
    x, y = nx, ny
    time += 1






