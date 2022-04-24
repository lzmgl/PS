# 5054번 주차의 신
# https://www.acmicpc.net/problem/5054
import sys, os
sys.stdin = open('{}/BOJ5054.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 5054번 주차의 신
# https://www.acmicpc.net/problem/5054
import sys
t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    stores=list(map(int, sys.stdin.readline().split()))
    print(2*(max(stores)-min(stores)))