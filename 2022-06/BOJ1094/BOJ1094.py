# 1094번 막대기
# https://www.acmicpc.net/problem/1094
import sys, os
sys.stdin = open('{}/BOJ1094.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
s = (bin(N)[2:])
ans=0
for i in s:
    if int(i):
        ans+=1
print(ans)