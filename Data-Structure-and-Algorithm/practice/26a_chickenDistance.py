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


n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

# print(graph)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def chicken_distance():
    x, y = 1, 1
    q = [(x, y)]
    nx = x + dx
    ny = y + dy
    if 1 <= nx or nx <= n or 1 <= ny or ny <= n:
        if graph[nx][ny] == 1:
            px = nx
            py = ny

        elif graph[nx][ny] == 2:
            pass
        else:
            pass
    else:
        pass
