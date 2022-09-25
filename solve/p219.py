#-*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
dp = [INF] * (n+1)
dp[1] = 0

for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)
    dp[i] = min(dp[i-1] + 1, dp[i])
    print(f'{i} -> {dp[i]}')
print(dp[n])