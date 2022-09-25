#-*- coding: utf-8 -*-
from collections import deque

INF = int(1e9)
n, m = 6, 11
start = 1
graph = [
    [],
    [(2, 2), (3, 5), (4, 1)],   #1
    [(3, 3), (4, 2)],           #2
    [(2, 3), (6, 5)],           #3
    [(3, 3), (5, 1)],           #4
    [(3, 1), (6, 2)],           #5
    []
]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

queue = deque()
queue.append(start)
distance[start] = 0
`
while queue:
    current = queue.popleft()
    visited[current] = True
    for a, d in graph[current]:
        distance[a] = min(distance[current] + d, distance[a])
        if not visited[a]:
            queue.append(a)

for i in range(1, n+1):
    print(distance[i])



