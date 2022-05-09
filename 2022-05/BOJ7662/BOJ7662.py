# 7662번 이중 우선순위 큐
# https://www.acmicpc.net/problem/7662
import sys, os
sys.stdin = open('{}/BOJ7662.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import heapq
def Insert(q, num):
    heapq.heappush(q, num)
def Delete(q, num):
    heapq.heappop(q)

T=int(sys.stdin.readline())
for _ in range(T):
    k=int(sys.stdin.readline())
    visited=[False]*k
    minq, maxq = [], []
    for j in range(k):
        p, num = sys.stdin.readline().split()
        num=int(num)
        if p == 'I':
            Insert(minq, (num, j))
            Insert(maxq, (-num, j))
            visited[j]=True
        else:
            if num==1:
                while maxq and not visited[maxq[0][1]]:
                    heapq.heappop(maxq)
                if maxq:
                    visited[maxq[0][1]]=False
                    heapq.heappop(maxq)
            else:
                while minq and not visited[minq[0][1]]:
                    heapq.heappop(minq)
                if minq:
                    visited[minq[0][1]]=False
                    heapq.heappop(minq)
    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)
    if not minq or not maxq:
        print("EMPTY")
    else:
        print(-maxq[0][0], minq[0][0])