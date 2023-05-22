# 1504번 특정한 최단 경로
# https://www.acmicpc.net/problem/1504
import sys, os
from collections import defaultdict
import heapq
INF = int(1e9)

def dijkstra(graph, start, end):
    distance = [INF]*(N+1)
    distance[start] = 0
    q = [(0,start)]
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]] : 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

sys.stdin = open('{}/BOJ1504.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, E=map(int, sys.stdin.readline().split())
net = defaultdict(list)
for _ in range(E):
    a, b, c = map(int , sys.stdin.readline().split())
    net[a].append((b, c))
    net[b].append((a, c))
v1, v2 = map(int , sys.stdin.readline().split())

path1 = dijkstra(net, 1,  v1) + dijkstra(net, v1, v2) + dijkstra(net, v2, N)
path2 = dijkstra(net, 1,  v2) + dijkstra(net, v2, v1) + dijkstra(net, v1, N)

total = min(path1, path2)

if total >= INF : 
    print(-1)
else : print(total)


