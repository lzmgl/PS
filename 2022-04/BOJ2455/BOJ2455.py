# 2455번 지능형 기차
# https://www.acmicpc.net/problem/2455
import sys, os
sys.stdin = open('{}/BOJ2455.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2455번 지능형 기차
# https://www.acmicpc.net/problem/2455
import sys
people=maxN=0
for _ in range(4):
    a, b=map(int, sys.stdin.readline().split())
    people+=b-a
    maxN=max(maxN,people)
print(maxN)