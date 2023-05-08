# 16928번 뱀과 사다리 게임
# https://www.acmicpc.net/problem/16928
import sys, os
sys.stdin = open('{}/BOJ16928.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
N, M=map(int,sys.stdin.readline().split())
ledder = [0 for _ in range(106)]
snake = [0 for _ in range(106)]
visited = [999 for _ in range(106)]
q=deque([1])
visited[0]=0
visited[1]=0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    ledder[x]=y
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    snake[x]=y

while q:
    if visited[100]!=999:
        print(visited[100])
        break
    pos=q.popleft()
    for i in range(1,7):
        if pos+i<=100 and visited[pos+i]==999:

            if ledder[pos+i]==0 and snake[pos+i]==0: #사다리 뱀 없으면
                q.append(pos+i)
                visited[pos+i]=visited[pos]+1
            elif snake[pos+i]!=0: #뱀 있으면
                q.append(snake[pos+i])
                visited[snake[pos+i]]=min(visited[pos]+1, visited[snake[pos+i]])
                visited[pos+i]=visited[pos]+1
            else:
                q.append(ledder[pos+i]) #사다리 있으면
                visited[ledder[pos+i]]=min(visited[pos]+1, visited[ledder[pos+i]])
                visited[pos+i]=visited[pos]+1
