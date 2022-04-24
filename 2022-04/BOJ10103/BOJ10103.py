# 10103번 주사위 게임
# https://www.acmicpc.net/problem/10103
import sys, os
sys.stdin = open('{}/BOJ10103.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
S=C=100
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a<b:
        S-=b
    elif a>b:
        C-=a
print(S, C)