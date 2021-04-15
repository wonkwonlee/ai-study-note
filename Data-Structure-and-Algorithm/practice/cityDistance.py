"""
City Distance
"""

from collections import deque

# n nodes, m edges, k target distance, x starting node
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# Store input in the graph
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# Store distance to each city
distance = [-1] * (n + 1)
# Distance from X city to X city is always 0
distance[x] = 0

# BFS algorithm
q = deque([x])

while q:
    curr = q.popleft()
    for next_node in graph[curr]:
        if distance[next_node] == -1:
            distance[next_node] = distance[curr] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check is False:
    print(-1)
