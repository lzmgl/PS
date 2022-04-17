# 2606번 바이러스
# https://www.acmicpc.net/problem/2606
import sys, os
    
sys.stdin = open('{}/BOJ2606.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
graph={}

def DFS(graph, root):
    stack=[root]
    visited=[]
    
    while stack:
        n=stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n])-set(visited))
                tmp.sort(reverse=True)
                stack+=tmp
                
    return (len(visited)-1)


for _ in range(M):
    n1, n2= map(int, sys.stdin.readline().split())
    if n1 not in graph:
        graph[n1]=[n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
    if n2 not in graph:
        graph[n2]=[n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(DFS(graph, 1))