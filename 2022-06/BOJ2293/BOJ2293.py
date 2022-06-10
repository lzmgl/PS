# 2293번 동전 1
# https://www.acmicpc.net/problem/2293
import sys, os
sys.stdin = open('{}/BOJ2293.txt'.format(os.path.dirname(os.path.realpath(__file__))))
n, k=map(int, sys.stdin.readline().split())
data=[int(sys.stdin.readline()) for _ in range(n)]
data=[0]+data
dp=[0]*(k+1)
dp[0]=1
for i in range(1, n+1):
    for j in range(data[i], k+1):
        dp[j]+=dp[j-data[i]]
print(dp[k])