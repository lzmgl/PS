# 2530번 인공지능 시계
# https://www.acmicpc.net/problem/2530
import sys, os
sys.stdin = open('{}/BOJ2530.txt'.format(os.path.dirname(os.path.realpath(__file__))))
h, m, s = map(int, sys.stdin.readline().split())
d = int(sys.stdin.readline())
dh=0
ds = d%60
dm = d//60
if dm//60 >0:
    dh = dm//60
    dm = dm%60
dh+=h
dm+=m
ds+=s
d+=s
while d>59:
    d-=60
    m+=1
    if m>59:
        m-=60
        h+=1
        if h>23:
            h-=24
print(h, m, d)
'''
while ds>59:
    ds-=60
    dm+=1
while dm>59:
    dm-=60
    dh+=1
while dh>23:
    dh-=24
print(dh, dm, ds)
'''