# 2522번 별 찍기 - 12
# https://www.acmicpc.net/problem/2522
import sys, os
sys.stdin = open('{}/BOJ2522.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())N=int(input())
for i in range(1,N): 
    print(' '*(N-i), '*'*i, sep='')
for i in range(N,0,-1): 
    print(' '*(N-i), '*'*i, sep='')