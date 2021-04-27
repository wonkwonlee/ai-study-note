"""
City Distance

# Example
4 4 2 1
1 2 
1 3 
2 3 
2 4

>> 4
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
distance[x] = 0 # distance -> [-1, 0, -1, -1, -1]

# BFS algorithm
q = deque([x])

while q:
    # now: current searching node
    now = q.popleft()
    for next_node in graph[now]:
        # Check if current node is unvisited
        if distance[next_node] == -1:
            # Increase distance to current node by 1
            # distance[now] -> 0, distance[next_node] -> 1
            # distance[now] -> 1, distance[next_node] -> 2
            distance[next_node] = distance[now] + 1
            # Search for next node
            q.append(next_node)

# distance -> [-1, 0, 1, 1, 2]
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        # Set check True if any node has distance of k
        check = True

# If none of node has distance of k, print -1
if check is False:
    print(-1)
