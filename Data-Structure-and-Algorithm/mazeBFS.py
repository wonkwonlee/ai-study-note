'''
Test Case
5 6 
101010
111111
000001
111111
111111

>> 10

deque : double-endedd queue, which can handle data in both ends.
'''
from collections import deque

# Length = N, Width = M
N, M = map(int, input().split())
# Map info in 2-D list
graph = []

# move directions
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Fill graph with values
for i in range(N):
    graph.append(list(map(int, input())))

# BFS method
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # While queue is not empty
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # Ignore out of bound
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # Ignore if current node is corner
            if graph[nx][ny] == 0:
                continue
            # Store the shortest path only if it is the first vist
            if graph[nx][ny] == 1:
                # print((x,y), graph[x][y])
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # Print graph with each cost
    # print(graph)  
    return graph[N-1][M-1]
    
print(bfs(0, 0))