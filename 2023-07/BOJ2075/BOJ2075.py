# 2075번 N번째 큰 수
# https://www.acmicpc.net/problem/2075
import sys, os
sys.stdin = open('{}/BOJ2075.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import heapq
N=int(sys.stdin.readline())
ans=[]
for _ in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    for c in tmp:
        if len(ans)>=N:
            heapq.heappushpop(ans, c)
        else:
            heapq.heappush(ans, c)
print(ans[0])