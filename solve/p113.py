#-*- coding: utf-8 -*-
N = int(input())
walk = list(input().split())

coord = [1, 1]
for _walk in walk:
    if _walk == 'L' and coord[1] > 1:
        coord[1] = coord[1] - 1
    elif _walk == 'R' and coord[1] < N:
        coord[1] = coord[1] + 1
    elif _walk == 'U' and coord[0] > 1:
        coord[0] = coord[0] - 1
    elif _walk == 'D' and coord[0] < N:
        coord[0] = coord[0] + 1

print(coord)
