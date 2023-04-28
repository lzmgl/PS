# 1182번 부분수열의 합
# https://www.acmicpc.net/problem/1182
import sys, os
sys.stdin = open('{}/BOJ1182.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from itertools import combinations
N, S=map(int,sys.stdin.readline().split())
data=list(map(int, sys.stdin.readline().split()))
ans=0
for i in range(1,N+1):
    res = list(combinations(data, i))
    for item in res:
        if S==(sum(item)):
            ans+=1
print(ans)