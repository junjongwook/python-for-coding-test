#-*- coding: utf-8 -*-
INF = int(1e9)
n = 5
m = 7

graph = [[INF] * (n + 1) for _ in range(n+1)]
graph[1][2] = 1
graph[1][3] = 1
graph[1][4] = 1
graph[2][4] = 1
graph[3][4] = 1
graph[3][5] = 1
graph[4][5] = 1

x = 4
k = 5

for i in range(n+1):
    for j in range(n+1):
        if i == j: graph[i][j] = 0
        else:
            graph[i][j] = min(graph[i][j], graph[j][i])

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            distance = graph[j][i] + graph[i][k]
            if distance < graph[j][k]:
                graph[j][k] = distance

def print_graph():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF:
                print('N', end=' ')
            else:
                print(graph[i][j], end=' ')
        print()
print_graph()

result = graph[1][k] + graph[k][x]
if result >= INF:
    result = -1
print(result)

