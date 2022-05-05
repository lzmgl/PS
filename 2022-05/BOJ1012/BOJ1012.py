# 1012번 유기농 배추
# BFS dx dy 상하좌우 4방향 미로찾기
# https://www.acmicpc.net/problem/1012
import sys, os
sys.stdin = open('{}/BOJ1012.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import collections
T=int(sys.stdin.readline())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def BFS(graph, root_arr, cnt):
    queue=collections.deque([root_arr])
    while queue:
        x, y=queue.popleft()
        for i in range(4):
           nx, ny =  x+dx[i], y+dy[i]
           if N>nx>=0 and M>ny>=0 and visited[nx][ny]==-1:
               if graph[nx][ny]>0:
                   queue.append([nx, ny])
                   visited[nx][ny]=cnt
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    visited = [[-1]*M for _ in range(N)]
    farm = [[0]*M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        farm[x][y] = 1
    cnt=0
    for i in range(N):
        for j in range(M):
            if farm[i][j] > 0 and visited[i][j]<0:
                cnt+=1
                BFS(farm, [i,j], cnt)
    print(cnt)