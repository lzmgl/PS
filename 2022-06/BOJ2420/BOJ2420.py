# 2420번 사파리월드
# https://www.acmicpc.net/problem/2420
import sys, os
sys.stdin = open('{}/BOJ2420.txt'.format(os.path.dirname(os.path.realpath(__file__))))
a, b=map(int,sys.stdin.readline().split())
print(abs(a-b))