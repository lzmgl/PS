# 10156번 과자
# https://www.acmicpc.net/problem/10156
import sys, os
sys.stdin = open('{}/BOJ10156.txt'.format(os.path.dirname(os.path.realpath(__file__))))
K,N,M = map(int,sys.stdin.readline().split())
res=K*N-M
if res > 0:
    print(res)
else:
    print("0")