# 2579번 계단 오르기
# https://www.acmicpc.net/problem/2579
import sys, os
sys.stdin = open('{}/BOJ2579.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[0]*301
for i in range(1, N+1):
    data[i] = int(sys.stdin.readline())
dp=[0]*301
dp[1]=data[1]
dp[2]=data[1]+data[2]
dp[3]=max(data[1],data[2])+data[3]
for i in range(4, N+1):
    dp[i]=max(dp[i-2]+data[i], dp[i-3]+data[i-1]+data[i])
print(dp[N])