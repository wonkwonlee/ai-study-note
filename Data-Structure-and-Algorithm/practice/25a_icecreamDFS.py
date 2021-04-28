"""
Icecream DFS Search

# Example
4 5
00110
00011
11111
00000
>> 3

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
>> 8
"""

# N row, M column
n, m = map(int, input().split())

graph = []
for i in range(n):
    # Add input N input lines
    graph.append(list(map(int, input())))


# DFS algorithm
def dfs(x, y):
    # Return False if out of boundary
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # If coordinate is 0, it is unvisited
    if graph[x][y] == 0:
        # Mark visited coordinate as 1
        graph[x][y] = 1
        # Recursive search
        dfs(x - 1, y)   # -1, 0
        dfs(x + 1, y)   # 1, 0
        dfs(x, y - 1)   # 0, -1
        dfs(x, y + 1)   # 0, 1
        # Return True if all recursive method are True
        return True

    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
