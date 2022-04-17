# 2178번 미로 탐색
# BFS 미로 각각 list에 넣어 visited, deque, [4][2]방향전환.
# https://www.acmicpc.net/problem/2178
import sys, os
sys.stdin = open('{}/BOJ2178.txt'.format(os.path.dirname(os.path.realpath(__file__))))

N, M=map(int,sys.stdin.readline().split())
maze = [ list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N) ]
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]
queue=deque([[0,0]])
visited = [ [-1]*M for _ in range(N) ]
x, y = queue[0][0], queue[0][1]
visited[0][0]=1

while queue:
    x, y=queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if N>nx>=0 and M>ny>=0 and visited[nx][ny]==-1:
            if maze[nx][ny]>0:
                queue.append([nx,ny])
                visited[nx][ny]=visited[x][y]+1

print(visited[N-1][M-1])