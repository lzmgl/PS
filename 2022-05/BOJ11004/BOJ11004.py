# 11004번 K번째 수
# https://www.acmicpc.net/problem/11004
import sys, os
sys.stdin = open('{}/BOJ11004.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, K=map(int,sys.stdin.readline().split())
data=list(map(int, sys.stdin.readline().split()))
data.sort()
print(data[K-1])