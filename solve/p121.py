#-*- coding: utf-8 -*-
N, M = list(map(int, input().split()))
x, y, d = list(map(int, input().split()))

visited = [[0] * M for _ in range(N)]
for n in range(N):
    visited[n] = list(map(int, input().split()))

# print(sea)
direction = 0
dd = [(-1, 0), (0, -1), (1 ,0), (0, 1)]
result = 0
while True:
    move = False
    visited[x][y] = 1
    result += 1
    for _ in range(4):
        nx = x + dd[direction][0]
        ny = y + dd[direction][1]
        if visited[nx][ny] == 0:
            move = True
            x, y = nx, ny
            break
        else:
            direction = (direction + 1) % 4
    if not move: break

print(result)