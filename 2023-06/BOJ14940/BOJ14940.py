# 14940번 쉬운 최단거리
# https://www.acmicpc.net/problem/14940
import sys, os
sys.stdin = open('{}/BOJ14940.txt'.format(os.path.dirname(os.path.realpath(__file__))))

from collections import deque
def sol():
    
    def bfs(data, root):
        q=deque()
        q.append((root[1],root[0]))
        while q:
            cy, cx = q.popleft()

            for i in range(4):
                ny, nx = cy+dy[i], cx+dx[i]
                if 0<=ny<n and 0<=nx<m and data[ny][nx]==-1:
                    data[ny][nx]=data[cy][cx]+1
                    q.append((ny,nx))
    n, m=map(int,sys.stdin.readline().split())
    data=[]
    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    for i in range(n):
        tmp=list(map(int,sys.stdin.readline().split()))
        for j in range(m):
            if tmp[j]==2:
                x=j
                y=i
                tmp[j]-=2
            else:
                tmp[j]-=2
        data.append(tmp)

    bfs(data, [x,y])
    for item in data:
        for j in range(m):
            if item[j]==-2:
                item[j]=0

    for item in data:
        print(*item)

    
if __name__ == '__main__':
    sol()
