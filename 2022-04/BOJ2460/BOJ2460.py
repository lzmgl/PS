# 2460번 지능형 기차 2
# https://www.acmicpc.net/problem/2460
import sys, os
sys.stdin = open('{}/BOJ2460.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2460번 지능형 기차2
# https://www.acmicpc.net/problem/2460
import sys
people=maxN=0
for _ in range(10):
    a, b=map(int, sys.stdin.readline().split())
    people+=b-a
    maxN=max(maxN,people)
print(maxN)