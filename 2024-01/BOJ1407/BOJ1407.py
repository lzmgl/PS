# 1407번 2로 몇 번 나누어질까
# https://www.acmicpc.net/problem/1407
import sys, os
sys.stdin = open('{}/BOJ1407.txt'.format(os.path.dirname(os.path.realpath(__file__))))
a, b=map(int,sys.stdin.readline().split())

def f(x):
    ans=0
    y=0
    i=1
    while x>0:
        if x&1:
            y=x//2 + 1
        else:
            y=x//2
        ans+=y*i
        x-=y
        i*=2
    return ans
print(f(b)-f(a-1))