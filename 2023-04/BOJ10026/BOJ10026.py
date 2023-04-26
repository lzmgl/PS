# 10026번 적록색약
# https://www.acmicpc.net/problem/10026

import sys, os
sys.setrecursionlimit(100001)
sys.stdin = open('{}/BOJ10026.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
graph=[sys.stdin.readline().strip() for i in range(N)]
graph2=[]

for item in graph:
    graph2.append(item.replace("G",'R'))

visited = [[False] * N for _ in range(N)]
visited2=[[False] * N for _ in range(N)]
cnt=0
cnt2=0
dy=[0,0,1,-1]
dx=[1,-1,0,0]
ans=[]
ans2=[]
nowLetter=''
nowLetter2=''
def DFS(graph ,y, x, nowLetter, visited):
    global cnt
    visited[y][x]=True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<N and 0<=ny<N:
            if graph[ny][nx]==nowLetter and visited[ny][nx]==False:
                visited[ny][nx]=True
                cnt+=1
                DFS(graph, ny, nx, nowLetter, visited)

for j in range(N):
    for i in range(N):
        if nowLetter != graph[j][i] and visited[j][i]==False:
            nowLetter=graph[j][i]
        if graph[j][i] == nowLetter and visited[j][i]==False:
            cnt+=1
            DFS(graph, j, i, nowLetter, visited)
            ans.append(cnt)
            cnt=0
for j in range(N):
    for i in range(N):
        if nowLetter2 != graph2[j][i] and visited2[j][i]==False:
            nowLetter2=graph2[j][i]
        if graph2[j][i] == nowLetter2 and visited2[j][i]==False:
            cnt2+=1
            DFS(graph2, j, i, nowLetter2, visited2)
            ans2.append(cnt2)
            cnt2=0

print(len(ans),len(ans2))