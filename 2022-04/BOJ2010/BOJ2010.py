# 2010번 플러그
# https://www.acmicpc.net/problem/2010
import sys, os
sys.stdin = open('{}/BOJ2010.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2010번 플러그
# https://www.acmicpc.net/problem/2010
import sys
N=int(sys.stdin.readline())
tmp=0
for _ in range(N):
    s=int(sys.stdin.readline())
    tmp+=s
tmp-=(N-1)
print(tmp)