# 1012번 유기농 배추
# https://www.acmicpc.net/problem/1012
import sys, os
sys.stdin = open('{}/BOJ1012.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    farm = [[0]*M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        farm[x][y] = 1
    for item in farm:
        print(item)
    print('============')