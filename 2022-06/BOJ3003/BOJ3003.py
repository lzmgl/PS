# 3003번 킹, 퀸, 룩, 비숍, 나이트, 폰
# https://www.acmicpc.net/problem/3003
import sys, os
sys.stdin = open('{}/BOJ3003.txt'.format(os.path.dirname(os.path.realpath(__file__))))
ans=[1, 1, 2, 2, 2, 8]
data=list(map(int, sys.stdin.readline().split()))
ret=[]
for i in range(len(ans)):
    ret.append(ans[i]-data[i])
print(*ret)