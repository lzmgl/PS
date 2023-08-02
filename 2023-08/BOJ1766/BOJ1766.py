# 1766번 문제집
# https://www.acmicpc.net/problem/1766
import sys, os
sys.stdin = open('{}/BOJ1766.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import defaultdict
import heapq
net=defaultdict(list)
N, M=map(int,sys.stdin.readline().split())
indegree=[0]*(N+1)
q=[]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    indegree[b]+=1

for i in range(1, N+1):
    if indegree[i]==0:
        heapq.heappush(q,i)

answer=[]
while q:
    now = heapq.heappop(q)
    answer.append(now)
    for item in net[now]:
        indegree[item]-=1
        if indegree[item]==0:
            heapq.heappush(q,item)
print(*answer)