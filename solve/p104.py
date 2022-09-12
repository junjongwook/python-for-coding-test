#-*- coding: utf-8 -*-
N, K = list(map(int, input().split()))

result = 0
while True:
    temp = (N // K) * K
    result = result + (N - temp)
    N = temp
    if N < K: break
    N = N // K
    result = result + 1

result = result + (N - 1)
print(result)