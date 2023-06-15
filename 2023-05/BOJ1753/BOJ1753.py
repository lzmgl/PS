# 1753번 최단경로
# https://www.acmicpc.net/problem/1753
import sys, os
sys.stdin = open('{}/BOJ1753.txt'.format(os.path.dirname(os.path.realpath(__file__))))
def sol():
    from collections import defaultdict
    import heapq
    INF = int(1e15)
    def dijkstra(graph, start):
        distance = [INF]*(E+3)
        distance[start] = 0
        q = [(0,start)]
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                print(f"i = {i}")
                print(f"distance = {distance}")
                cost = dist + i[1]
                if cost < distance[i[0]] : 
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance

    V, E=map(int,sys.stdin.readline().split())
    K=int(sys.stdin.readline())
    net=defaultdict(list)
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        net[u].append((v,w))
    tmp = (dijkstra(net, K))
    for i in range(1, V+1):
        if tmp[i]==INF:
            print('INF')
            continue
        print(tmp[i])
if __name__ == '__main__':
    sol()