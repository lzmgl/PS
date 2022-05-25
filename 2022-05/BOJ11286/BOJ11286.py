# 11286번 절댓값 힙
# heapq
# https://www.acmicpc.net/problem/11286
import sys, os
sys.stdin = open('{}/BOJ11286.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import heapq
N=int(sys.stdin.readline())
heap=[]
for _ in range(N):
    x = int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(heap, (abs(x), x)) #절대값 트릭
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)