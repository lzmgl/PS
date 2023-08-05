# 1916번 최소비용 구하기 다익스트라 Dijkstra
# https://www.acmicpc.net/problem/1916
import sys, os

sys.stdin = open("{}/BOJ1916.txt".format(os.path.dirname(os.path.realpath(__file__))))

from collections import defaultdict
import heapq


def sol():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    net = defaultdict(list)
    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        net[u].append((w, v))
    start, end = map(int, sys.stdin.readline().split())

    def dijkstra(s, end):
        pq = []
        visited = [float("inf")] * (N + 1)
        heapq.heappush(pq, (0, s))
        while pq:
            cost, now = heapq.heappop(pq)
            if visited[now] < cost:
                continue
            for w, v in net[now]:
                next_w = cost + w

                if visited[v] > next_w:
                    heapq.heappush(pq, (next_w, v))
                    visited[v] = next_w
        return visited[end]

    print(dijkstra(start, end))


if __name__ == "__main__":
    sol()
