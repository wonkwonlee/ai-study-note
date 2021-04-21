"""
Square Travel

Input1: N size of square
Input2: Move directions L, R, U, D
Output: Final destination

# Example
5
R R R U D D
>> 3 4
"""


# n = 5
n = int(input())
moves = input().split()

# Move directions L(0,-1), R(0,1), U(-1,0), D(1,0)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = ['L', 'R', 'U', 'D']

# Initial point
x, y = 1, 1

# Check every move in moves
for move in moves:
    # Operate each move by direction
    for i in range(len(direction)):
        if move == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # Ignore out of boundary
    if nx < 1 or nx >= n or ny < 1 or ny >= n:
        continue
    # Update x, y if valid
    else:
        x, y = nx, ny

print(x, y)
