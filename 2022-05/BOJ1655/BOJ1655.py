# 1655번 가운데를 말해요
# https://www.acmicpc.net/problem/1655
import sys, os
sys.stdin = open('{}/BOJ1655.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import heapq
N=int(sys.stdin.readline())
maxh=[]
minh=[]
for _ in range(N):
    x=int(sys.stdin.readline())
    if len(maxh)==0:
        heapq.heappush(maxh, (-x, x))
    else:
        if len(maxh)>len(minh):
            heapq.heappush(minh, x)
        else:
            heapq.heappush(maxh, (-x, x))
    try:
        if maxh[0][1]>minh[0]:
            a = heapq.heappop(maxh)
            b = heapq.heappop(minh)
            heapq.heappush(maxh, (-b, b))
            heapq.heappush(minh, a[1])
    except:
        pass
    print(maxh[0][1])