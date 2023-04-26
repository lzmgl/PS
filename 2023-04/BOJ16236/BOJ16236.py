# 16236번 아기 상어
# https://www.acmicpc.net/problem/16236
import sys, os
sys.stdin = open('{}/BOJ16236.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
from collections import deque
M=N
net=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

dy=[0,0,1,-1]
dx=[1,-1,0,0]
size=2
def checkFood(size, visited):
    min_time=99999999
    for i in range(N):
        for j in range(N):
            if 1<=net[i][j]<size and visited[i][j] != -1:
                if visited[i][j]<min_time:
                    min_time=visited[i][j]
                    ny,nx = i, j
    if min_time==99999999:
        return False, -1, -1, min_time
    return True, ny, nx, min_time
isOne=False
y, x = 0,0
for i in range(N):
    for j in range(N):
        if net[i][j]==9:
            y, x = i, j
            net[i][j]=0
        if net[i][j]==1:
            isOne=True

cnt=size
ans=0
if not isOne:
    print(ans)
    exit()

q=deque()
def bfs():
    visited=[[-1]*M for _ in range(N)]
    visited[y][x]=0
    q.append((y,x))
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0<=ny<N and 0<=nx<N and visited[ny][nx]==-1:
                if net[ny][nx]<=size:
                    visited[ny][nx]=visited[cy][cx]+1
                    q.append((ny,nx))

    return visited


while True:
    check = checkFood(size, bfs())
    if not check[0]:
        print(ans)
        break
    else:
        y,x=check[1], check[2]
        ans+=check[3]
        net[y][x]=0
        cnt-=1
    if cnt==0:
        size+=1
        cnt=size