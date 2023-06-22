# 21736번 헌내기는 친구가 필요해
# https://www.acmicpc.net/problem/21736
import sys, os
sys.stdin = open('{}/BOJ21736.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
def sol():
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    N, M=map(int,sys.stdin.readline().split())
    data=[]
    for i in range(N):
        tmp=sys.stdin.readline().strip()
        row=[]
        for j in range(M):
            if tmp[j]=='O':
                row.append(0)
            elif tmp[j]=='X':
                row.append(-1)
            elif tmp[j]=='I':
                y=i
                x=j
                row.append(0)
            else:
                row.append(1)
        data.append(row)
    
    def bfs():
        ans=0
        visited=[[-1]*M for _ in range(N)]
        q=deque()
        q.append((y,x))
        while q:
            cy, cx = q.popleft()
            for i in range(4):
                ny, nx=cy+dy[i], cx+dx[i]
                if 0<=ny<N and 0<=nx<M and visited[ny][nx]==-1:
                    if data[ny][nx]>=0:
                        q.append((ny,nx))
                        visited[ny][nx]+=1
                        if data[ny][nx]==1:
                            ans+=1
        if ans==0:
            ans='TT'
        return ans

    print(bfs())
if __name__=='__main__':
    sol()