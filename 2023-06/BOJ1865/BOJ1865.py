# 1865번 웜홀 벨만포드 가중치음수
# https://www.acmicpc.net/problem/1865
import sys, os
sys.stdin = open('{}/BOJ1865.txt'.format(os.path.dirname(os.path.realpath(__file__))))
def bellman_ford(graph, start):
        distance, predecessor = dict(), dict()
        for node in graph:
            distance[node] = float('inf')
            predecessor[node] = None
        distance[start] = 0

        for i in range(len(graph)-1):
            for node in graph:
                for neighbor in graph[node]:
                    print(node)
                    print(graph[node])
                    print(neighbor)
                    print(distance[neighbor])
                    if distance[neighbor] > distance[node] + graph[node][neighbor]:
                        distance[neighbor]=distance[node]+graph[node][neighbor]
                        predecessor[neighbor] = node

        for node in graph:
            for neighbor in graph[node]:
                if distance[neighbor] > distance[node] + graph[node][neighbor]:
                    return -1
        return distance, predecessor
def sol():
    from collections import defaultdict
    TC=int(sys.stdin.readline())        
    
    
    for _ in range(TC):
        net=defaultdict(list)
        N, M, W = map(int, sys.stdin.readline().split())
        for j in range(M):
            u, v, w = map(int, sys.stdin.readline().split())
            net[u].append([v,w])
            net[v].append([u,w])
        for j in range(W):
            S, E, T = map(int, sys.stdin.readline().split())
            net[S].append([E,-T])
        print(bellman_ford(net, 0))

        


if __name__ == '__main__':
    sol()
