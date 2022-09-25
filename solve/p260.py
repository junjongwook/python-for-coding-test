#-*- coding: utf-8 -*-
INF = int(1e9)

n = 4
m = 7

graph = [[INF] * (n + 1) for _ in range(n + 1)]
graph[1][2] = 4
graph[1][4] = 6
graph[2][1] = 3
graph[2][3] = 7
graph[3][1] = 5
graph[3][4] = 4
graph[4][3] = 2

for i in range(n + 1):
    graph[i][i] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: continue
        for k in range(1, n+1):
            if i == k or j == k: continue
            new_distance = graph[j][i] + graph[i][k]
            if new_distance < graph[j][k]:
                graph[j][k] = new_distance

def print_graph():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF:
                print('N', end=' ')
            else:
                print(graph[i][j], end=' ')
        print()
print_graph()

