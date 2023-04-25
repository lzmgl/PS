# 11724번 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
import sys, os
sys.setrecursionlimit(5000)
sys.stdin = open('{}/BOJ11724.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N,M=map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    src, dst = (map(int, sys.stdin.readline().split()))
    graph[src].append(dst)
    graph[dst].append(src)

def DFS(start, depth, visited):
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            DFS(i, depth+1, visited)

visited = [False]*(1+N)
cnt=0

for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            cnt+=1
            visited[i]=True
        else:
            DFS(i, 0, visited)
            cnt+=1
print(cnt)