# 2506번 점수계산
# https://www.acmicpc.net/problem/2506
import sys, os
sys.stdin = open('{}/BOJ2506.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2506번
# https://www.acmicpc.net/problem/2506
import sys
cnt=res=0
N=int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
for item in data:
    cnt=(cnt+1)*item
    res+=cnt
print(res)