# 9325번 얼마?
# https://www.acmicpc.net/problem/9325
import sys, os
sys.stdin = open('{}/BOJ9325.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())T=int(input())
for _ in range(T):
    s=int(input())
    n=int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        q*=p
        s+=q
    print(s)
    