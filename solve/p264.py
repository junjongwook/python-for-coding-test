#-*- coding: utf-8 -*-
INF = int(1e9)
n, m, c = 3, 2, 1

graph = [[INF] * (n + 1) for _ in range(n+1)]
for i in range(n + 1):
    graph[i][i] = 0

graph[1][2] = 4
graph[1][3] = 2

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if i == j or i == k: continue
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

_max = 0
count = 0
for i in range(1, n + 1):
    if i == c: continue
    if graph[c][i] < INF:
        count += 1
        _max = max(graph[c][i], _max)

print(count, _max)

def print_graph():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:
                print('N', end=' ')
            else:
                print(graph[i][j], end=' ')
        print()


print_graph()
