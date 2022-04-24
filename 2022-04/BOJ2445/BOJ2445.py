# 2445번 별 찍기 - 8
# https://www.acmicpc.net/problem/2445
import sys, os
sys.stdin = open('{}/BOJ2445.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2445번 별 찍기 - 8
# https://www.acmicpc.net/problem/2445
N=int(input())
for i in range(-N+1,N):
    i=abs(i)
    print('*'*(N-i), ' '*(i*2), '*'*(N-i),sep='')