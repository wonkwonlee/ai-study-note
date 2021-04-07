# 최단 경로 알고리즘 Shortest Path Algorithm

## 최단 경로 문제 Shortest Path Problem
* *최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘*으로 **길 찾기 문제**라고도 불린다.
* 최단 경로 알고리즘 유형에는 다양한 종류가 있고 상황에 맞는 효율적인 알고리즘이 이미 정립되어 있다.
    + 예를 들어, *한 지점에서 다른 특징 지점까지의 최단 경로를 구해야 하는 경우* 혹은 *모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우* 등 다양한 사례가 존재한다.
    + 대표적인 최단 경로 알고리즘에는 **다익스트라(Dijkstra Algorithm), 플로이드 워셜(Floyd-Warshall Algorithm), 벨만 포드 알고리즘(Bellman-Ford Algorithm)** 등이 있다.
* 최단 경로 문제는 보통 그래프를 이용해 표현하는데 각 지점은 그래프에서 **노드(node)** 로 표현되고 지점간 연결된 도로는 그래프에서 **간선(edge)** 로 표현한다.
* 실제 코딩 테스트에서는 최단 경로를 모두 출력하는 문제보다는 *단순히 최단 거리를 출력하도록 요구하는 문제가 많이 출제*된다.
    + 그리디 알고리즘 및 다이나믹 프로그래밍 알고리즘이 최단 경로 알고리즘에 그대로 적용된다.


## 다익스트라 알고리즘 Dijkstra Algorithm
* 다익스트라 최단 경로 알고리즘은 그래프에서 여러 개의 노드가 있을 때 **특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로**를 구해 주는 알고리즘이다.
* 다익스트라 최단 경로 알고리즘은 **음의 간선**이 없을 때 정상적으로 동작한다.
    + 음의 간선이란 0보다 작은 값을 가지는 간선을 의미한다. 
    + 현실 세계의 길은 음의 간선으로 표현되지 않으므로 *다익스트라 알고리즘은 실제로 GPS 소프트웨어의 기본 알고리즘으로 채택*된다.
* 다익스트라는 매번 *가장 비용이 적은 노드를 선택해서 임의의 과정을 반복*하기 때문에 기본적으로 그리디 알고리즘으로 분류된다.

### 다익스트라 알고리즘의 작동 원리
1. **출발 노드**를 설정한다.
2. 최단 거리 테이블을 초기화 한다.
3. 방문하지 않은 노드 중에서 **최단 거리가 가장 짧은 노드를 선택**한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 **최단 거리 테이블을 갱신**한다.
5. 위의 과정에서 3, 4번을 반복한다.

* 다익스트라 알고리즘은 **각 노드에 대한 현재까지의 최단 거리** 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신한다.
* 다시 말해, 현재 처리하고 있는 노드를 기준으로 주변 간선을 확인하고 나중에 더 짧은 경로를 찾으면 갱신한다.

<img width="498" alt="spp" src="https://user-images.githubusercontent.com/28593767/113644114-ef705080-96be-11eb-9d08-2d1c7173deb2.png">

> 출발 노드를 1이라고 할 때, 1번 노드에서 다른 모든 노드로의 최단 거리를 계산한다. 
>
> 초기 상태에서는 *다른 모든 노드로 가는 최단 거리를 무한으로 초기화*한다.

<img width="689" alt="dijk0" src="https://user-images.githubusercontent.com/28593767/113794762-442ace80-9786-11eb-91d2-ffbccaac29b9.png">

<img width="413" alt="d0" src="https://user-images.githubusercontent.com/28593767/113794998-d337e680-9786-11eb-9be1-9e8e1a322080.png">

<img width="689" alt="dijk1" src="https://user-images.githubusercontent.com/28593767/113794768-45f49200-9786-11eb-9dd2-b956771cd5b7.png">

<img width="413" alt="d1" src="https://user-images.githubusercontent.com/28593767/113795000-d3d07d00-9786-11eb-9c15-e11c586812ef.png">

<img width="689" alt="dijk2" src="https://user-images.githubusercontent.com/28593767/113794769-468d2880-9786-11eb-9104-3c6e444f8599.png">

<img width="413" alt="d2" src="https://user-images.githubusercontent.com/28593767/113795003-d4691380-9786-11eb-91b2-576aea1f0055.png">

<img width="689" alt="dijk3" src="https://user-images.githubusercontent.com/28593767/113794772-47be5580-9786-11eb-9042-cdf3e2bfb32d.png">

<img width="413" alt="d3" src="https://user-images.githubusercontent.com/28593767/113795006-d501aa00-9786-11eb-8cf8-0275f3f1024d.png">

<img width="689" alt="dijk4" src="https://user-images.githubusercontent.com/28593767/113794773-47be5580-9786-11eb-8aae-f809240d97ab.png">

<img width="413" alt="d4" src="https://user-images.githubusercontent.com/28593767/113795007-d501aa00-9786-11eb-82b9-de5d7a1219c5.png">

<img width="689" alt="dijk5" src="https://user-images.githubusercontent.com/28593767/113794766-455bfb80-9786-11eb-869e-c9a4c6aa9c1c.png">

<img width="413" alt="d5" src="https://user-images.githubusercontent.com/28593767/113794995-d0d58c80-9786-11eb-93c0-d4e33c68141b.png">

<img width="689" alt="dijk6" src="https://user-images.githubusercontent.com/28593767/113794771-4725bf00-9786-11eb-9dbf-b81777f5fb4e.png">

<img width="413" alt="d6" src="https://user-images.githubusercontent.com/28593767/113794997-d206b980-9786-11eb-9491-c8d4de03eebc.png">

### 간단한 다익스트라 알고리즘
* 다익스트라에 의해 처음 고안된 알고리즘으로 직관적이고 이해하기 쉽다.
* V는 노드의 개수를 의미하고 각 노드에 대한 최단 거리를 담는 1차원 리스트를 선언한다.
* **각 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 순차 탐색으로 확인**한다.
* 모든 리스트는 **(노드의 개수 + 1)의 크기로 할당하여 노드의 번호를 인덱스**로 하여 바로 리스트에 접근한다.

```python
import sys
input = sys.stdin.readline
INF = int(1e9)

# N is the number of node and M is the number of edge
n, m = map(int, input().split())
# Starting node position
start = int(input())
graph = [[] for i in range(n + 1)]

# Initialize all node to be unvisited
visited = [False] * (n + 1)
# Initialize current distance to be infinity
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # For each node index, store edge to the neighboring node
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]: 
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1] 
            if cost < distance[j[0]]: 
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

'''
INPUT
6 11
1
1 2 2; 1 3 5; 1 4 1; 2 3 3; 2 4 2; 3 2 3; 3 6 5; 4 3 3; 4 5 1; 5 3 1; 5 6 2

OUTPUT
0; 2; 3; 1; 2; 4
'''
```







