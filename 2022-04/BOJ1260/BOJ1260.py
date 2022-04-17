# 1260번 DFS와 BFS
# 양뱡향 그래프 생성과 DFS BFS
# https://www.acmicpc.net/problem/1260
import sys, os

sys.stdin = open('{}/BOJ1260.txt'.format(os.path.dirname(os.path.realpath(__file__))))

from collections import deque
def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)


N, M, V=map(int, (sys.stdin.readline().split()))
graph={}
for _ in range(M):
    src, dst = (map(int, sys.stdin.readline().split()))
    if src not in graph:
        graph[src]=[dst]
    elif dst not in graph[src]:
        graph[src].append(dst)

    if dst not in graph:
        graph[dst]=[src]
    elif dst not in graph[dst]:
        graph[dst].append(src)

print(DFS(graph, V))
print(BFS(graph, V))