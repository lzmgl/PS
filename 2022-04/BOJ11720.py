# 11720번 숫자의 합
# https://www.acmicpc.net/problem/11720
import sys
sumN=0
input()
N=sys.stdin.readline().rstrip()
for i in N:
    sumN+=int(i)
print(sumN)