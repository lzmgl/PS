# 6064번 카잉 달력
# https://www.acmicpc.net/problem/6064
import sys, os
sys.stdin = open('{}/BOJ6064.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
def ans(m,n,x,y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    print(ans(M,N,x,y))