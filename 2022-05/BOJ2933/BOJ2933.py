# 2933번 미네랄
# https://www.acmicpc.net/problem/2933
import sys, os
sys.stdin = open('{}/BOJ2933.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque

R, C=map(int,sys.stdin.readline().split())

def BFS(graph, root_arr, cnt):
    queue=deque([root_arr])
    clusters=[]
    clusters.append(tuple(root_arr))
    y, x = root_arr
    visited[y][x]=cnt
    while queue:
        y, x=queue.popleft()
        for i in range(4):
           nx, ny =  x+dx[i], y+dy[i]
           if C>nx>=0 and R>ny>=0 and visited[ny][nx]==-1 and graph[ny][nx]=='x':
                queue.append([ny, nx])
                clusters.append((ny,nx))
                visited[ny][nx]=cnt
    return clusters
                   
cave = [list(sys.stdin.readline().strip()) for _ in range(R)]
N=int(sys.stdin.readline())
height=list(map(int, sys.stdin.readline().split()))
    
dy=[0,0,1,-1]
dx=[1,-1,0,0]

cnt=0
for i, c in enumerate(height):
    isBreak=False
    visited = [[-1]*C for _ in range(R)]
    if i%2 == 0:
        for idx in range(C):
            data=cave[R-c][idx]
            if data=='x':
                isBreak=True
                cave[R-c][idx]='.'
                x, y = idx, R-c
                break
    else:
        for idx in range(C-1, -1, -1):
            data=cave[R-c][idx]
            if data=='x':
                isBreak=True
                cave[R-c][idx]='.'
                x, y = idx, R-c
                break
    down=[]
    if isBreak:
        for idx in range(4):
            nx, ny = x+dx[idx], y+dy[idx]
            if C > nx >= 0 and R > ny >= 0:
                if cave[ny][nx]=='x' and visited[ny][nx]<0:
                    cnt+=1
                    cl = BFS(cave, [ny, nx], cnt)
                    if cl:
                        cl.sort(reverse=True)
                        if (max(cl)[0])==R-1:
                            continue
                        else: #공중에 뜸!
                            down.append(cl)
                    else:
                        continue
        for change in down:
            for ny, nx in change:
                cave[ny][nx]='.'
            
            rest=R-1-change[0][0]
            for ny, nx in change:
                for p in range(ny+1, R):
                    if cave[p][nx] == 'x' and p-ny-1<rest:
                        rest=min(p-ny-1, rest)
            for ny, nx in change:
                cave[ny+rest][nx]='x'
for x in cave:
    print(''.join(x))