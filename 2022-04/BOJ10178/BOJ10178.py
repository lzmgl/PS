# 10178번 할로윈의 사탕
# https://www.acmicpc.net/problem/10178
import sys, os
sys.stdin = open('{}/BOJ10178.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    print(f"You get {a//b} piece(s) and your dad gets {a%b} piece(s).")