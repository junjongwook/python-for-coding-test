#-*- coding: utf-8 -*-
N, K = list(map(int, input().split()))

result = 0
while True:
    if N == 1: break
    if N % K == 0:
        N = N // K
        result += 1
    else:
        N = N - 1
        result +=  1
print(result)
