# 2523번 별 찍기 - 13
# https://www.acmicpc.net/problem/2523
import sys, os
sys.stdin = open('{}/BOJ2523.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())N=int(input())
for i in range(1,N): 
    print('*'*i)
for i in range(N,0,-1): 
    print('*'*i)