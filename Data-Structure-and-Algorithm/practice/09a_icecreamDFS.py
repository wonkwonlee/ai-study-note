"""
Test case
4 5
00110
00011
11111
00000

# DFS
"""


def dfs(graph, x, y):
    # Validation check
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # If x,y is unvisited, then it is visited now
    if graph[x][y] == 0:
        graph[x][y] = 1
        # Use recursions to search neighboring nodes
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False


n, m = map(int, input().split())
graph = []

# Fill graph with values
for i in range(n):
    graph.append(list(map(int, input())))

# print(graph)
# [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

# Run DFS method for all graph nodes
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):  # if dfs(i, j) is True
            result += 1

print(result)
