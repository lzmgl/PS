# 1010번 다리 놓기
# https://www.acmicpc.net/problem/1010
from math import factorial
import sys, os
from itertools import combinations
sys.stdin = open('{}/BOJ1010.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
for _ in range(T):
    M, N = map(int, sys.stdin.readline().split())
    print(factorial(N)//(factorial(N-M)*factorial(M)))