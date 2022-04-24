# 2446번 별 찍기 - 9
# https://www.acmicpc.net/problem/2446
import sys, os
sys.stdin = open('{}/BOJ2446.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2446번 별 찍기 - 8
# https://www.acmicpc.net/problem/2446
N=int(input())
for i in range(-N+1,N):
    i=abs(i)
    print(' '*(N-i-1), '*'*(2*(i)+1),sep='')