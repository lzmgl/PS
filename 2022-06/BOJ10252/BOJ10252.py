# 10252번 그리드 그래프
# https://www.acmicpc.net/problem/10252
import sys, os
sys.stdin = open('{}/BOJ10252.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(1)
    for i in range(m):
        print(f'(0,{i})')
    for i in range(1, n):
        if i%2:
            for j in range(m-1, 0, -1):
                print(f'({i},{j})')
        else:
            for j in range(1, m):
                print(f'({i},{j})')
    for i in range(n-1, 0, -1):
        print(f'({i},0)')