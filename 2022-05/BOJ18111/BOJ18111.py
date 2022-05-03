# 18111번 마인크래프트
# https://www.acmicpc.net/problem/18111

import sys, os
sys.stdin = open('{}/BOJ18111.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import math
N, M, B=map(int,sys.stdin.readline().split())
data=[]
for _ in range(N):
    tmp=(list(map(int, sys.stdin.readline().split())))
    for item in tmp:
        data.append(item)
data.sort(reverse=True)
ans=[0]*257
for height in range(257):
    block=B
    for item in data:
        if item > height:
            ans[height] += (item-height)*2
            block+=(item - height)
        if item < height:
            if block>=(height-item):
                ans[height]+=(height-item)
                block -= (height-item)
            else:
                ans[height] += math.inf
                break
ans.reverse()
print(min(ans), 256-ans.index(min(ans)))