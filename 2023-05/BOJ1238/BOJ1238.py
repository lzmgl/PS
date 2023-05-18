# 1238번 파티 DFS, 다익스트라
# https://www.acmicpc.net/problem/1238
import sys, os
sys.stdin = open('{}/BOJ1238.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import heapq
from collections import defaultdict



def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph} # initialize distances to infinity
    distances[start] = 0 # set starting vertex distance to 0
    heap = [(0, start)] # initialize heap with starting vertex and its distance
    visited = set() # initialize visited set
    
    while heap:
        (current_distance, current_vertex) = heapq.heappop(heap) # extract minimum distance vertex
        if current_vertex in visited: # skip if already visited
            continue
         # mark current vertex as visited
        
        visited.add(current_vertex)
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]: # update distance if shorter path is found
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor)) # add neighbor to heap with its new distance
                
    return distances

N, M, X=map(int,sys.stdin.readline().split())
net = defaultdict(list)
for _ in range(M):
    p, q, r = (map(int, sys.stdin.readline().split()))
    net[p].append((q, r))

result=[]
for i in range(1,N+1):
    tmp=dijkstra(net, i)
    result.append(tmp)

maxN=0
for i in range(0, N):
    maxN=max(maxN, result[i][X]+result[X-1][i+1])

print(maxN)