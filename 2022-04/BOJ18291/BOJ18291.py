# 18291번 비요뜨의 징검다리 건너기
# https://www.acmicpc.net/problem/18291
import sys, os
    
sys.stdin = open('{}/BOJ18291.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    if N!=1:
        print(pow(2,N-2,1000000007))
    else:
        print(1)