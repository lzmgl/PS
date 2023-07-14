# 11501번 주식
# https://www.acmicpc.net/problem/11501
import sys, os
sys.stdin = open('{}/BOJ11501.txt'.format(os.path.dirname(os.path.realpath(__file__))))
t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    data=list(map(int, sys.stdin.readline().split()))
    ans=0
    maxN=0
    j=len(data)-1
    while j>-1:
        sellpoint = (data[j])
        j-=1
        while j>-1 and (sellpoint-data[j])>=0:
            maxN+=sellpoint-data[j]
            j-=1
    ans=max(ans, maxN)
    print(ans)