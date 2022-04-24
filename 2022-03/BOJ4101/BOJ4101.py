# 4101번 크냐?
# https://www.acmicpc.net/problem/4101
import sys, os
sys.stdin = open('{}/BOJ4101.txt'.format(os.path.dirname(os.path.realpath(__file__))))
while 1:
    a,b = map(int,sys.stdin.readline().split())
    if a==0:
        break
    if a>b:
        print("Yes")
    else:
        print("No")