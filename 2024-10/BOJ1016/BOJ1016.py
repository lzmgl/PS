# 1016번 제곱 ㄴㄴ 수
# https://www.acmicpc.net/problem/1016
import sys, os, math
sys.stdin = open('{}/BOJ1016.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, M=map(int,sys.stdin.readline().split())
data = [x**2 for x in range(2, int(M**0.5)+1)]
num=[1]*(M-N+1)
for item in data:
    n = N//item**2
    while(n<M+1):
        if n-N>=0:
            num[n-N]=0
        n+=item
print(sum(num))