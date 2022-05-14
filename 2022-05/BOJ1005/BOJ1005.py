# 1005번 ACM Craft
# https://www.acmicpc.net/problem/1005
import sys, os
sys.stdin = open('{}/BOJ1005.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
from collections import deque
for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    indegree=[0]*(V+1)
    graph=[ [] for i in range(V+1)]
    dp=[0]*(V+1)
    d_list = list(map(int, sys.stdin.readline().split()))
    d_list=[0]+d_list
    for i in range(E):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        indegree[y]+=1
    w=int(sys.stdin.readline())
    q=deque()
    for i in range(1, V+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        cur=q.popleft()
        if cur==w:
            print(dp[cur]+d_list[cur])
        for i in graph[cur]:
            indegree[i]-=1
            dp[i]=max(dp[i], dp[cur]+d_list[cur])
            if indegree[i]==0:
                q.append(i)