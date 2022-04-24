# 10886번 0 = not cute / 1 = cute
# https://www.acmicpc.net/problem/10886
import sys, os
sys.stdin = open('{}/BOJ10886.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
tmp=0
for _ in range(N):
    tmp+=int(input())
print('Junhee is'+[' not',''][N/2<tmp]+' cute!') 