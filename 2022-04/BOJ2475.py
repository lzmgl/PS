# 2475번 검증수
# https://www.acmicpc.net/problem/2475
import sys
sumN=0
numbers=list(map(int,sys.stdin.readline().split()))
for item in numbers:
    sumN+=item*item
print(sumN%10)