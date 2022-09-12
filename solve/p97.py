#-*- coding: utf-8 -*-

n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

block_count = m // (k+1)
rest_count = m % (k+1)

result = block_count * (first * k + second) + rest_count * first
print(result)

