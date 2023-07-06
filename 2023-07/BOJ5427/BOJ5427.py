# 5427번 불
# https://www.acmicpc.net/problem/5427
import sys, os
sys.stdin = open('{}/BOJ5427.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def sol():
    def bfs(w,h,start, data, fire):
        q=deque(fire)
        live=False
        while q:
            y, x = q.popleft()
            if data[y][x]=='*':
                data[y][x]=0
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0<=ny<h and 0<=nx<w:
                    if data[ny][nx] == '.' or data[y][x] == '@':
                        data[ny][nx] = data[y][x]+1
                        q.append((ny,nx))
        q=deque()
        q.append(start)
        while q:
            y, x = q.popleft()
            if data[y][x]=='@':
                data[y][x]=0
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0<=ny<h and 0<=nx<w:
                    if type(data[ny][nx])==int:
                        if data[y][x]+1<data[ny][nx]:
                            data[ny][nx]=data[y][x]+1
                            q.append([ny, nx])
                            
                            if ny==0 or ny==(h-1) or nx==0 or nx==(w-1):
                                live=True

                    elif data[ny][nx]=='.':
                        data[ny][nx]=data[y][x]+1
                        q.append((ny,nx))
                        if ny==0 or ny==(h-1) or nx==0 or nx==(w-1):
                            live=True
                else:
                    live=True
                    return data, live
        
        q=deque(fire)
        while q:
            y, x = q.popleft()
            data[y][x]=1000000
        data[start[0]][start[1]]=1000000
        return data, live


    T=int(sys.stdin.readline().strip())
    for _ in range(T):
        data=[]
        fire=[]
        end=False
        w,h=map(int,sys.stdin.readline().split())
        for i in range(h):
            tmp=list(sys.stdin.readline().strip())
            for j in range(w):
                if tmp[j]=='@':
                    if i==0 or i==h-1 or j==0 or j==w-1:
                        end = True
                    start=(i,j)
                elif tmp[j]=='*':
                    fire.append((i,j))
            data.append(list(tmp))

        if end:
            print(1)
            continue

        
        data, live = bfs(w,h,start, data, fire)
        maxN=0
        for i in range(h):
            for j in range(w):
                if i==0 or i==(h-1) or j==0 or j==(w-1):
                    if type(data[i][j])==int:
                        maxN=max((data[i][j]%1000000)+1, maxN)
        
        if not live:
            print("IMPOSSIBLE")
        else:
            print(maxN)

if __name__=='__main__':
    sol()