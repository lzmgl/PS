# 1202번 보석 도둑
# https://www.acmicpc.net/problem/1202
import sys, os
sys.stdin = open('{}/BOJ1202.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import heapq
N, K=map(int,sys.stdin.readline().split())
data=[]
# data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    heapq.heappush(data, list(map(int,sys.stdin.readline().split())))
bags = [int(sys.stdin.readline()) for _ in range(K)]
bags.sort()
ans=0
price_data=[]
for bag in bags:
    while data and bag >= data[0][0]:
        heapq.heappush(price_data, (-1)*heapq.heappop(data)[1])
    if price_data:
        ans += (-1)*heapq.heappop(price_data)
    elif not data:
        break
print(ans)