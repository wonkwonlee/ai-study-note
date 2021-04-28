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

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

>> 21
"""


# N size of square board, K number of apples
n = int(input())    # n = 6
k = int(input())    # k = 3

# N x N square board
graph = [[0] * (n + 1) for _ in range(n + 1)]

# Mark apples as 1
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

# print(graph)

# L number of changing directions
l = int(input())    # l = 3

# List to store turning information
info = []           # info = [(3, D), (15, L), (17, D)]
for _ in range(l):
    i, j = input().split()
    info.append((int(i), j))

# Move directions, x is vertical and y is horizontal
# Facing right-side at first (East, South, West, North)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs_snake():
    # Initial state
    x, y = 1, 1
    # Mark snake as 2
    graph[x][y] = 2
    # Moving direction is initially east
    direction = 0
    # Store time in second
    time = 0
    # Index for info array
    index = 0
    q = [(x, y)]    # [(1, 1)]

    while True:
        # (1,1) -> (1,2) -> (1,3) -> (1,4) -> (2,4) -> ...
        nx = x + dx[direction]
        ny = y + dy[direction]
        # print("Current snake position nx, ny : ", nx, ny)
        # Out of boundary (Square size: N+1 * N+1)
        if nx < 1 or nx > n or ny < 1 or ny > n or graph[nx][ny] == 2:
            time += 1
            break
        else:
            if graph[nx][ny] == 0:
                # Mark snake's new position as 2
                graph[nx][ny] = 2
                # Add a new position to the queue
                q.append((nx, ny))
                # Use pop(0) to pop the first element in the queue
                px, py = q.pop(0)
                # Update previous position as empty by marking 0
                graph[px][py] = 0

            # If new position is apple
            if graph[nx][ny] == 1:
                # Increase snake body and mark as 2
                graph[nx][ny] = 2
                # Add a new position to the queue
                q.append((nx, ny))

        # Update current position to a new position
        x, y = nx, ny
        time += 1

        # If it is time to turn, change direction
        # info[index][0] -> 3, 15, 17
        # index = 0, l = 0, info = [(3, D), (15, L), (17, D)]
        if index < l and time == info[index][0]:
            # Update direction by running turn function
            direction = turn(direction, info[index][1])
            index += 1

    return time


# Define turn function
def turn(direction, c):
    # If c == 'L', turn left 
    if c == 'L':
        direction = (direction - 1) % 4
    # If c == 'D', turn right
    else:
        direction = (direction + 1) % 4

    return direction


print(dfs_snake())
