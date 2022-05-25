# 1927번 최소 힙
# https://www.acmicpc.net/problem/1927
import sys, os
sys.stdin = open('{}/BOJ1927.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import heapq
N=int(sys.stdin.readline())
heap=[]
for _ in range(N):
    x = int(sys.stdin.readline())
    if x>0:
        heapq.heappush(heap, x)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)