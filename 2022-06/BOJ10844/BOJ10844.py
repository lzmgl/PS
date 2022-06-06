# 10844번 쉬운 계단 수
# https://www.acmicpc.net/problem/10844
import sys, os
sys.stdin = open('{}/BOJ10844.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
mod=1000000000
dp=[[0]*10 for _ in range(101)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, 101):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%mod

print(sum(dp[N])%mod)
