# 7662번 이중 우선순위 큐
# https://www.acmicpc.net/problem/7662
import sys, os
sys.stdin = open('{}/BOJ7662.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import heapq
def Insert(q, num):
    heapq.heappush(q, num)
def Delete(q, num):
    if num==1:
        maxV = max(q)
        q.remove(maxV)
    elif num==-1:
        heapq.heappop(q)

T=int(sys.stdin.readline())
for _ in range(T):
    k=int(sys.stdin.readline())
    q = []
    for _ in range(k):
        p, num = sys.stdin.readline().split()
        num=int(num)
        if p == 'I':
            Insert(q, num)
        else:
            try:
                Delete(q, num)
            except:
                continue
    if q:
        print(max(q), q[0])
    else:
        print("EMPTY")
        