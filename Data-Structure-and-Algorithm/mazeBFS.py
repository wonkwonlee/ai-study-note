'''
Test Case
5 6 
101010
111111
000001
111111
111111
'''
def dfs(x, y):
    # Validation check
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False



    return False

# Length = n, Width = m
n, m = map(int, input().split())
graph = []

# Fill graph with values
for i in range(n):
    graph.append(list(map(int, input())))

# # print(graph); [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j):   # if dfs(i, j) is True
#             result += 1

# print(result)

print(graph)