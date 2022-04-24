# 2921번 도미노
# https://www.acmicpc.net/problem/2921
import sys, os
sys.stdin = open('{}/BOJ2921.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())import sys
N=int(sys.stdin.readline())
print(((N*(N+1))//2)*(N+2))