# 11726번 2×n 타일링
# DP, 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/11726
import sys, os
sys.stdin = open('{}/BOJ11726.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from itertools import combinations
from math import factorial
N=int(sys.stdin.readline())
mod=10007
pos=N//2
DP=[0]*(N+1)
DP[0]=1
for i in range(pos+1):
    col=N-(2*i)
    DP[i]=(DP[i-1]+factorial(i+col)//(factorial(i)*factorial(col)))%mod

print(DP[N//2])