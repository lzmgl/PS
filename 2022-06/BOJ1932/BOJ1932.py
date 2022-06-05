# 1932번 정수 삼각형
# https://www.acmicpc.net/problem/1932
import sys, os
sys.stdin = open('{}/BOJ1932.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp=[[0]*N for _ in range(N)]
dp[0][0]+=data[0][0]
idx=0
for i in range(1, N):
    for j in range(i+1):
        dp[i][j]=data[i][j]+(max(dp[i-1][j-1], dp[i-1][j]))
print(dp)
print(max(dp[N-1]))