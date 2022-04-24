# 5717번 상근이의 친구들
# https://www.acmicpc.net/problem/5717
import sys, os
sys.stdin = open('{}/BOJ5717.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())while (s:=input())>'0 0':
    a,b=map(int, s.split())
    print(a+b)