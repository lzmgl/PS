# 15486번 퇴사 2
# https://www.acmicpc.net/problem/15486
import sys, os
sys.stdin = open('{}/BOJ15486.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
t=[0]*(N+2)
p=[0]*(N+2)
for i in range(1,N+1):
    t[i], p[i] = map(int, sys.stdin.readline().split())
dp=[0]*(N+2)
for i in range(1,N+1):
    if i+t[i]<=N+1:
        dp[i+1]=max(dp[i], dp[i+1])
        dp[i+t[i]]=max(dp[i]+p[i], dp[i+t[i]])
    else:
        dp[i+1]=max(dp[i+1], dp[i])
print(dp[N+1])