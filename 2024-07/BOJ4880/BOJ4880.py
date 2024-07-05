# 4880번 다음수
# https://www.acmicpc.net/problem/4880
import sys, os
sys.stdin = open('{}/BOJ4880.txt'.format(os.path.dirname(os.path.realpath(__file__))))
while(1):
    ans=0
    a,b,c=map(int, sys.stdin.readline().split())
    if a==b==c==0:
        break
    if c-b == b-a:
        ans=c+(b-a)
        print(f"AP {ans}")
    else:
        ans=c*(b//a)
        print(f"GP {ans}")