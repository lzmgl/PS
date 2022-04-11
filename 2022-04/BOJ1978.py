# 403 Forbidden
# https://www.acmicpc.net/problem/1978
import sys
N=int(sys.stdin.readline())
number=list(map(int, sys.stdin.readline().split()))
for item in number:
    if item<2:
        N-=1
        continue
    for i in range(2,item):
        if item%i==0:
            N-=1
print(N)