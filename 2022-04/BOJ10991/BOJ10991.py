# 10991번 별 찍기 - 16
# https://www.acmicpc.net/problem/10991
import sys, os
sys.stdin = open('{}/BOJ10991.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for i in range(1,N+1):
    print(' '*(N-i),'* '*i, sep='')