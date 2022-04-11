# 2506번
# https://www.acmicpc.net/problem/2506
import sys
cnt=res=0
N=int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
for item in data:
    cnt=(cnt+1)*item
    res+=cnt
print(res)