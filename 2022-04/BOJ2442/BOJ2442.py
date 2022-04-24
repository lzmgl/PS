# 2442번 별 찍기 - 5
# https://www.acmicpc.net/problem/2442
import sys, os
sys.stdin = open('{}/BOJ2442.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2442번 별 찍기 - 5
# https://www.acmicpc.net/problem/2442
N=int(input())
for i in range(1,N+1): 
    print(' '*(N-i), '*'*((i*2)-1), sep='')