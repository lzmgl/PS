# 2667번 단지번호붙이기
# https://www.acmicpc.net/problem/2667
import sys, os
sys.stdin = open('{}/BOJ2667.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
graph=[sys.stdin.readline().strip() for i in range(N)]
visited = [[False] * N for _ in range(N)]
cnt=0
dy=[0,0,1,-1]
dx=[1,-1,0,0]
ans=[]
def DFS(y, x):
    global cnt
    visited[y][x]=True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<N and 0<=ny<N:
            if graph[ny][nx]=='1' and visited[ny][nx]==False:
                visited[ny][nx]=True
                cnt+=1
                DFS(ny, nx)


for j in range(N):
    for i in range(N):
        if graph[j][i] == '1' and visited[j][i]==False:
            cnt+=1
            DFS(j, i)
            ans.append(cnt)
            cnt=0
ans.sort()
print(len(ans))
for item in ans:
    print(item)