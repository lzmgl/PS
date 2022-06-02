# 11049번 행렬 곱셈 순서
# DP, 다이나믹프로그래밍
# https://www.acmicpc.net/problem/11049
import sys, os
sys.stdin = open('{}/BOJ11049.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
tmp=[]
for _ in range(N):
    tmp.append(list(map(int, sys.stdin.readline().split())))
DP = [[0] * N for _ in range(N)]

for i in range(1, N):
    for start in range(0, N-i):
        end= start+i
        
        if start!=end:
            DP[start][end] = 2**31
        
        for k in range(start, end):
            DP[start][end]=min(DP[start][end], DP[start][k] + DP[k+1][end] + tmp[start][0]*tmp[k][1]*tmp[end][1])

print(DP[0][N-1])