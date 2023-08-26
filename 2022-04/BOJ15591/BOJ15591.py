# 15591번 MooTube (Silver)
# BFS 최소신장트리 MST graph defaultdict
# https://www.acmicpc.net/problem/15591
import sys, os

sys.stdin = open("{}/BOJ15591.txt".format(os.path.dirname(os.path.realpath(__file__))))
from collections import defaultdict, deque

N, Q = map(int, sys.stdin.readline().split())
net = defaultdict(list)


def moo(start_node, k, N, net):
    queue = deque()
    queue.append((start_node, 1000000000))
    visited = [-1] * (N + 1)
    visited[start_node] = 1
    cnt = 0
    while queue:
        current, minN = queue.popleft()
        for next_node, dst in net[current]:
            if visited[next_node] == 1:
                continue
            if minN > dst:
                queue.append((next_node, dst))
                if dst >= k:
                    cnt += 1
            else:
                queue.append((next_node, minN))
                if minN >= k:
                    cnt += 1
            visited[current] = 1
    return cnt


for _ in range(N - 1):
    p, q, r = map(int, sys.stdin.readline().split())
    net[p].append((q, r))
    net[q].append((p, r))
for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(moo(v, k, N, net))
