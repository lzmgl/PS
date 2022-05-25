# 11279번 최대 힙
# hepaq, 최대힙
# https://www.acmicpc.net/problem/11279
import sys, os
sys.stdin = open('{}/BOJ11279.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import heapq
N=int(sys.stdin.readline())
heap=[]
for _ in range(N):
    x = int(sys.stdin.readline())
    if x>0:
        heapq.heappush(heap, (-x, x)) #최대힙 트릭
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)