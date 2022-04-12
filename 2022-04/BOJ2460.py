# 2460번 지능형기차2
# https://www.acmicpc.net/problem/2460
import sys
people=maxN=0
for _ in range(10):
    a, b=map(int, sys.stdin.readline().split())
    people+=b-a
    maxN=max(maxN,people)
print(maxN)