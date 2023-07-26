# 21939번 문제 추천 시스템 Version 1
# https://www.acmicpc.net/problem/21939
import sys, os
sys.stdin = open('{}/BOJ21939.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import heapq
def Insert(q, num):
    heapq.heappush(q, num)
n=int(sys.stdin.readline())
minq, maxq = [], []
dickey={}
for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())
    Insert(minq, (l, p))
    Insert(maxq, (-l, -p))
    dickey[p]=True
    dickey[-p]=True

m=int(sys.stdin.readline())
for _ in range(m):
    do = sys.stdin.readline().split()
    if do[0]=='recommend':
        if (do[1])=='1':
            print(-maxq[0][1])
        else:
            print(minq[0][1])
    elif do[0]=='solved':
        # print("do[1] 번 문제 제거")
        dickey[int(do[1])]=False
        dickey[-int(do[1])]=False
        while maxq:
            l, p = heapq.heappop(maxq)
            if dickey[p]:
                Insert(maxq, (l, p))
                break
        while minq:
            l, p = heapq.heappop(minq)
            if dickey[p]:
                Insert(minq, (l, p))
                break
    else: # add
        Insert(minq, (int(do[2]), int(do[1])))
        Insert(maxq, (-int(do[2]), -int(do[1])))
        dickey[int(do[1])]=True
        dickey[-int(do[1])]=True
