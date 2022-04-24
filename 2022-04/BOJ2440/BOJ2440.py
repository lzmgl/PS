# 2440번 별 찍기 - 3
# https://www.acmicpc.net/problem/2440
import sys, os
sys.stdin = open('{}/BOJ2440.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2440번 별 찍기 - 3
# https://www.acmicpc.net/problem/2440
N=int(input())
for i in range(N,0,-1): 
    print('*'*i)