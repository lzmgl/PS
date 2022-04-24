# 1676번 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676
import sys, os
from math import factorial
sys.stdin = open('{}/BOJ1676.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
C=str(factorial(N))[::-1]
cnt=0
for c in C:
    if c == '0':
        cnt+=1
    else:
        break
print(cnt)