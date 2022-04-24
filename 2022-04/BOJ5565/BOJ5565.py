# 5565번 영수증
# https://www.acmicpc.net/problem/5565
import sys, os
sys.stdin = open('{}/BOJ5565.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())sum=int(input())
for _ in range(9):
    sum-=int(input())
print(sum)