#-*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
INF = int(1e9)

# n, m = list(map(int, input().split()))
# start = int(input())
# graph = [[] for i in range(n + 1)]
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

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

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

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
