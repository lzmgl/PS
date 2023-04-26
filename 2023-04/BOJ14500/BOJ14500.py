# 14500번 테트로미노
# https://www.acmicpc.net/problem/14500
import sys, os
sys.stdin = open('{}/BOJ14500.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, M=map(int,sys.stdin.readline().split())
net=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

tetris=[[(0,0),(0,1),(0,2),(0,3)],\
        [(0,0),(1,0),(2,0),(3,0)],\
        [(0,0),(1,0),(0,1),(1,1)],\
        [(0,0),(1,0),(2,0),(2,1)],\
        [(0,1),(1,1),(2,1),(2,0)],\
        [(0,0),(0,1),(1,1),(2,1)],\
        [(0,0),(0,1),(1,0),(2,0)],\
        [(0,0),(1,0),(1,1),(1,2)],\
        [(0,2),(1,1),(1,2),(1,0)],\
        [(0,0),(0,1),(0,2),(1,2)],\
        [(0,0),(1,0),(0,1),(0,2)],\
        [(0,0),(1,0),(1,1),(2,1)],\
        [(0,1),(1,1),(1,0),(2,0)],\
        [(1,0),(1,1),(0,1),(0,2)],\
        [(0,0),(0,1),(1,1),(1,2)],\
        [(0,1),(1,0),(1,1),(1,2)],\
        [(0,0),(0,1),(0,2),(1,1)],\
        [(0,0),(1,0),(1,1),(2,0)],\
        [(0,1),(1,1),(1,0),(2,1)]]

ans=0

for y in range(N):
    for x in range(M):

        for item in tetris:
            isBreak=False
            sum=0
            for tmp in item:
                ny, nx=y+tmp[0], x+tmp[1]
                if 0<=ny<N and 0<=nx<M:
                    sum+=net[ny][nx]
                else:
                    isBreak=True
                    break
            if isBreak:
                sum=0
                continue
            ans=max(ans, sum)
print(ans)