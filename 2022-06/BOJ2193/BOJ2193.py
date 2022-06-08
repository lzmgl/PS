# 2193번 이친수
# https://www.acmicpc.net/problem/2193
import sys, os
sys.stdin = open('{}/BOJ2193.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
dp=[0]*(N+1)
dp[1]=1
if N>1:
    dp[2]=1
if N>2:
    dp[3]=2
for i in range(2, N+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[N])