# 10953번 A+B - 6
# https://www.acmicpc.net/problem/10953
import sys, os
    
sys.stdin = open('{}/BOJ10953.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split(','))
    print(a+b)