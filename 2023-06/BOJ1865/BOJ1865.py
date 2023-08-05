# 1865번 웜홀 벨만포드 음수사이클
# https://www.acmicpc.net/problem/1865
import sys, os

sys.stdin = open("{}/BOJ1865.txt".format(os.path.dirname(os.path.realpath(__file__))))


def sol():
    from collections import defaultdict

    TC = int(sys.stdin.readline())

    for _ in range(TC):
        net = defaultdict(list)
        N, M, W = map(int, sys.stdin.readline().split())
        for _ in range(M):
            u, v, w = map(int, sys.stdin.readline().split())
            net[u].append([v, w])
            net[v].append([u, w])
        for _ in range(W):
            S, E, T = map(int, sys.stdin.readline().split())
            net[S].append([E, -T])

        def bellman_ford(graph, start):
            distances = [10001] * (N + 1)
            distances[start] = 0
            for i in range(N):
                for s in net:
                    for d, w in net[s]:
                        if distances[d] > distances[s] + w:
                            if i == (N - 1):
                                return "YES"
                            distances[d] = distances[s] + w
            return "NO"

        print(bellman_ford(net, 0))


if __name__ == "__main__":
    sol()
