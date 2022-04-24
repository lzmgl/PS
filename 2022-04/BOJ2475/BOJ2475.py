# 2475번 검증수
# https://www.acmicpc.net/problem/2475
import sys, os
sys.stdin = open('{}/BOJ2475.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2475번 검증수
# https://www.acmicpc.net/problem/2475
import sys
sumN=0
numbers=list(map(int,sys.stdin.readline().split()))
for item in numbers:
    sumN+=item*item
print(sumN%10)