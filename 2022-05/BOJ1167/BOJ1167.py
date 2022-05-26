# 1167번 트리의 지름
# https://www.acmicpc.net/problem/1167
import sys, os
sys.stdin = open('{}/BOJ1167.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque

N=int(sys.stdin.readline())
adj = [[] for _ in range(N)]
for _ in range(N):
    tmp=list(map(int, sys.stdin.readline().split()))
    V, *arr, _ = tmp
    for i in range(0, len(arr), 2):
        adj[V-1].append((arr[i]-1, arr[i+1]))
visited=[False]*(N)
def BFS(n):
    node, dist= 0, 0
    q=deque()
    q.append((n, 0))
    visited[n]=True
    while q:
        cur, cur_dist = q.popleft()
        for i in adj[cur]:
            if visited[i[0]]==False:
                visited[i[0]]=True
                sum_dist = cur_dist+i[1]
                q.append((i[0], sum_dist))

                if sum_dist>dist:
                    dist=sum_dist
                    node=i[0]
    return node, dist
a, b = BFS(0)
visited=[False]*(N)
print(BFS(a)[1])