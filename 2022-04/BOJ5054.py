# 5054번 주차의 신
# https://www.acmicpc.net/problem/5054
import sys
t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    stores=list(map(int, sys.stdin.readline().split()))
    print(2*(max(stores)-min(stores)))