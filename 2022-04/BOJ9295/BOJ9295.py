# 9295번 주사위
# https://www.acmicpc.net/problem/9295
import sys, os
sys.stdin = open('{}/BOJ9295.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())import sys
N=int(sys.stdin.readline())
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case {i+1}: {a+b}")