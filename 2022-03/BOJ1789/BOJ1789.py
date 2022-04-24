# 1789번 수들의 합
# https://www.acmicpc.net/problem/1789
import sys, os
sys.stdin = open('{}/BOJ1789.txt'.format(os.path.dirname(os.path.realpath(__file__))))
S = int(sys.stdin.readline())
cnt=0
while(S>cnt):
    cnt+=1
    S-=cnt
print(cnt)