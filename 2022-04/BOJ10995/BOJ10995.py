# 10995번 별 찍기 - 20
# https://www.acmicpc.net/problem/10995
import sys, os
sys.stdin = open('{}/BOJ10995.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for i in range(1,N+1):
    for j in range(1,N+1):
        print('*',end='')
        print(' ',end='')
    print()
    if i%2==1:
        print(' ',end='')