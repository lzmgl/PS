# 5427번 불
# https://www.acmicpc.net/problem/5427
import sys, os
sys.stdin = open('{}/BOJ5427.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def sol():
    q=deque(fire)
    while q:
        y, x = q.popleft()
        if visited[y][x] == -2: # 이게 불인지 사람인지 체크
            cnt=-2
        else:
            cnt=visited[y][x]
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<h and 0<=nx<w:
                # 불이든 사람이든 갈 수 있는 곳인지 체크
                if visited[ny][nx]==-1 and (data[ny][nx]=='.' or data[ny][nx]=='@'):
                    if cnt==-2: #불이면 불번지기
                        visited[ny][nx]=-2
                    else: # 사람이면 cnt+1로 가기
                        visited[ny][nx]=cnt+1
                    q.append((ny,nx))
            else: # 건물 경계임 = 통과할수있음
                if cnt!=-2: #불이 닿은게 아니라면 return (탈출성공)
                    return cnt+1
    return "IMPOSSIBLE" # q 끝날때까지 사람이 견물 경계에 못닿은 경우.

if __name__=='__main__':
    T=int(sys.stdin.readline().strip())
    for _ in range(T):
        data=[]
        fire=[]
        end=False
        w,h=map(int,sys.stdin.readline().split())
        visited=[[-1]*w for _ in range(h)]
        for i in range(h):
            data.append(list(sys.stdin.readline().strip()))
            for j in range(w):
                if data[i][j]=='@':
                    visited[i][j]=0
                    start=(i,j)
                elif data[i][j]=='*':
                    visited[i][j]=-2
                    fire.append((i,j))
        if end:
            print(1)
            continue
        fire.append(start) # 불 먼저 다 하고, start 하기
        print(sol())