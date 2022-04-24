# 9085번 더하기
# https://www.acmicpc.net/problem/9085
import sys, os
sys.stdin = open('{}/BOJ9085.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 9085번
# https://www.acmicpc.net/problem/9085
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    tmp=list(map(int, sys.stdin.readline().split()))
    print(sum(tmp))