# 2531번 회전 초밥
# https://www.acmicpc.net/problem/2531
import sys, os
sys.stdin = open('{}/BOJ2531.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
import itertools
N, d, k, c=map(int,sys.stdin.readline().split())
data=deque()
for _ in range(N):
    data.append(int(sys.stdin.readline().strip()))
maxN=0
for _ in range(N):
    ans=set(list(itertools.islice(data,0,k)))
    ans.add(c)
    maxN=max(maxN, len(ans))
    data.rotate(1)
print(maxN)