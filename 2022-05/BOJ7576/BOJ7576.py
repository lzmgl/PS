# 7576번 토마토
# BFS, 그래프탐색, 넓이우선탐색
# https://www.acmicpc.net/problem/7576
import sys, os
sys.stdin = open('{}/BOJ7576.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
M, N=map(int, sys.stdin.readline().split())
data=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

def BFS(que_list, graph):
    c=0
    while que_list:
        x, y, c = que_list.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if N>nx>=0 and M>ny>=0 and graph[nx][ny]>-1 and visit[nx][ny]<0:
                visit[nx][ny]=c+1
                que_list.append([nx, ny, c+1])
    for i in range(N):
        for j in range(M):
            if graph[i][j]>-1 and visit[i][j]==-1:
                return -1
    return c

minN=1001

visit=[[-1]*M for _ in range(N)]
tmp_list=deque()
for i,row in enumerate(data):
    for j,item in enumerate(row):
        if item == 1:
            tmp_list.append([i, j, 0])
            visit[i][j]=0
        elif item == -1:
            visit[i][j]=0
print(BFS(tmp_list, data))