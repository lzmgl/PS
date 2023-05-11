# 17626번 Four Squares
# https://www.acmicpc.net/problem/17626
import sys, os
sys.stdin = open('{}/BOJ17626.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
dp=[50001 for i in range(N+1)]
dp[0]=0
for i in range(1, N+1):
    for j in range(1, i+1):
        tmp=j**2
        if tmp>i:
            break
        dp[i]=min(dp[i], dp[i-tmp]+1)
print(dp[N])