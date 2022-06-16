# 24444번 알고리즘 수업 - 너비 우선 탐색 1
# https://www.acmicpc.net/problem/24444
import sys, os
sys.stdin = open('{}/BOJ24444.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import  deque
def BFS(start_node):
    queue=deque()
    queue.append(start_node)
    cnt=1
    visited[start_node]=cnt
    while queue:
        cur=queue.popleft()
        for next in net[cur]:
            if visited[next]==0:
                queue.append(next)
                cnt+=1
                visited[next]=cnt

N, M, R=map(int,sys.stdin.readline().split())
net=[[] for _ in range(N+1)]
visited=[0]*(N+1)

for _ in range(N):
    p, q = (map(int, sys.stdin.readline().split()))
    net[p].append(q)
    net[q].append(p)
for i in net:
    i.sort()
    
BFS(R)

for i in range(1, N+1):
    print(visited[i])