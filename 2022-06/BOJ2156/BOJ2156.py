# 2156번 포도주 시식
# https://www.acmicpc.net/problem/2156
import sys, os
sys.stdin = open('{}/BOJ2156.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[int(sys.stdin.readline()) for _ in range(N)]
dp=[0]*N
dp[0]=data[0]
dp[1]=data[0]+data[1]
dp[2]=max(dp[2-2]+data[2], data[2-1]+data[2], dp[2-1])
for i in range(3, N):
    dp[i]=max(dp[i-2]+data[i], dp[i-3]+data[i-1]+data[i], dp[i-1])
print(max(dp))