# 1865번 웜홀 벨만포드 가중치음수
# https://www.acmicpc.net/problem/1865
import sys, os
sys.stdin = open('{}/BOJ1865.txt'.format(os.path.dirname(os.path.realpath(__file__))))
def sol():
    from collections import defaultdict
    TC=int(sys.stdin.readline())        
    def bellman(graph, start):
        INF = int(1e15)
        distance = [INF]*(E+3)
        distance[start] = 0
        for v in graph:
            print(v,graph[v])
            for item in graph[v]:
                # u=item[0]
                # weight=item[1]
                print(item)
                # if v>
    for _ in range(TC):
        net=defaultdict(list)
        N, M, W = map(int, sys.stdin.readline().split())
        for j in range(M):
            u, v, w = map(int, sys.stdin.readline().split())
            net[u].append({v:w})
            net[v].append({u:w})
        for j in range(W):
            S, E, T = map(int, sys.stdin.readline().split())
            net[S].append({E:-T})
        bellman(net, 0)

        


if __name__ == '__main__':
    sol()
