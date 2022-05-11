# 7569번 토마토
# https://www.acmicpc.net/problem/7569
import sys, os
sys.stdin = open('{}/BOJ7569.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
M, N, H=map(int, sys.stdin.readline().split())

dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dh=[0,0,0,0,1,-1]

data=[]
for _ in range(H):
    tmp=[]
    for _ in range(N):
        tmp.append(list(map(int, sys.stdin.readline().split())))
    data.append(tmp)

def BFS(que_list, graph):
    c=0
    while que_list:
        h, y, x, c = que_list.popleft()
        for i in range(len(dx)):
            nx, ny, nh = x+dx[i], y+dy[i], h+dh[i]
            if M>nx>=0 and N>ny>=0 and H>nh>=0 and graph[nh][ny][nx]>-1 and visit[nh][ny][nx]>1000000:
                visit[nh][ny][nx]=min(c+1, visit[nh][ny][nx])
                que_list.append([nh, ny, nx, c+1])
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k]>-1 and visit[i][j][k]>1000000:
                    return -1

    return c

minN=1000001
visit=[[[minN]*M for _ in range(N)] for h in range(H)]
tmp_list=deque()
for i,row in enumerate(data):
    for j,column in enumerate(row):
        for k, item in enumerate(column):
            if item == 1:
                tmp_list.append([i, j, k, 0])
                visit[i][j][k]=0
            elif item == -1:
                visit[i][j][k]=0

print(BFS(tmp_list, data))