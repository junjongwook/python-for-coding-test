#-*- coding: utf-8 -*-
N, M = list(map(int, input().split()))
data = [[0] * M for _ in range(N)]
# print(data)
result = 0
for i in range(N):
    data[i] = list(map(int, input().split()))
    min_number = min(data[i])
    result = max(min_number, result)

print(result)
