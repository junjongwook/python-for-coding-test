# -*- coding: utf-8 -*-
N = int(input())
plans = list(input().split())

h, w = 1, 1

moves = ['L', 'R', 'U', 'D']
dh = [0, 0, -1, 1]
dw = [-1, 1, 0, 0]

for walk in plans:
    index = moves.index(walk)
    nx = h + dh[index]
    ny = w + dw[index]
    if 1 <= nx <= N and 1 <= ny <= N:
        h, w = nx, ny

print(h, w)