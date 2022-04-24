# 2443번 별 찍기 - 6
# https://www.acmicpc.net/problem/2443
import sys, os
sys.stdin = open('{}/BOJ2443.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2443번 별 찍기 - 6
# https://www.acmicpc.net/problem/2443
N=int(input())
for i in range(N,0,-1): 
    print(' '*(N-i), '*'*((i*2)-1), sep='')