# 11057번 오르막 수
# https://www.acmicpc.net/problem/11057
import sys, os
sys.stdin = open('{}/BOJ11057.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from math import factorial
mod=10007
N=int(sys.stdin.readline())
print((factorial(9+N)//(factorial(9)*factorial(N)))%mod)