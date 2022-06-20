# 2738번 행렬 덧셈
# https://www.acmicpc.net/problem/2738
import sys, os
sys.stdin = open('{}/BOJ2738.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, M=map(int,sys.stdin.readline().split())
A=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
B=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans=[]
for i in range(N):
    tmp=[]
    for j in range(M):
        tmp.append(A[i][j]+B[i][j])
    ans.append(tmp)

for item in ans:
    print(*item)