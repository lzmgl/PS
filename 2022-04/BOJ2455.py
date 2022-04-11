# 2455번
# https://www.acmicpc.net/problem/2455
import sys
people=maxN=0
for _ in range(4):
    a, b=map(int, sys.stdin.readline().split())
    people+=b-a
    maxN=max(maxN,people)
print(maxN)