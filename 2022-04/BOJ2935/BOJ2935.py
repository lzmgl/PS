# 2935번 소음
# https://www.acmicpc.net/problem/2935
import sys, os
sys.stdin = open('{}/BOJ2935.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())import sys
a=input()
b=input()
c=input()
if b=='*':
    print(a+c[1:])
else:
    if a==c:
        print(int(a)+int(c))
        exit()
    c='0b'+c
    a='0b'+a
    print(str(bin(int(a,2)+int(c,2)))[2:])