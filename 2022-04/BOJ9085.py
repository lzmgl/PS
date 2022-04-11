# 9085번
# https://www.acmicpc.net/problem/9085
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    tmp=list(map(int, sys.stdin.readline().split()))
    print(sum(tmp))