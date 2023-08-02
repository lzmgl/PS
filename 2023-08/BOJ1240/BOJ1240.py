# 1240번 노드사이의 거리
# https://www.acmicpc.net/problem/1240
import sys, os
sys.stdin = open('{}/BOJ1240.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import defaultdict, deque
N, M=map(int,sys.stdin.readline().split())
net=defaultdict(list)
for _ in range(N-1):
    a, b, d = map(int, sys.stdin.readline().split())
    net[a].append((b,d))
    net[b].append((a,d))
answer=[]
def bfs(start, end):
    q=deque()
    visited=[0]*(N+1)
    q.append((start,0))
    visited[start]=1
    while q:
        n2, d = q.popleft()
        if n2 == end:
            return d

        for n, distance in net[n2]:
            if not visited[n]:
                visited[n]=1
                q.append((n, distance+d))
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    answer.append(bfs(start, end))
for item in answer:
    print(item)