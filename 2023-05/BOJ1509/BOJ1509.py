# 1509번 팰린드롬 분할
# https://www.acmicpc.net/problem/1509
import sys, os
sys.stdin = open('{}/BOJ1509.txt'.format(os.path.dirname(os.path.realpath(__file__))))

data = sys.stdin.readline().strip()
n = len(data)

is_p = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dp = [float('inf')] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    is_p[i][i] = 1

for i in range(1, n):
    if data[i-1] == data[i]:
        is_p[i][i+1] = 1

for i in range(2, n):
    for j in range(1, n+1-i):
        if data[j-1] == data[j+i-1] and is_p[j+1][i+j-1] == 1:
            is_p[j][i+j] = 1

for i in range(1, n+1):
    dp[i] = min(dp[i], dp[i-1] + 1)
    
    for j in range(i+1, n+1):
        if is_p[i][j] != 0:
            dp[j] = min(dp[j], dp[i-1] + 1)
print(dp[n])