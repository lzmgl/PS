# 10872번 팩토리얼
# https://www.acmicpc.net/problem/10872
import sys, os
sys.stdin = open('{}/BOJ10872.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from math import factorial
N=int(sys.stdin.readline())
print(factorial(N))