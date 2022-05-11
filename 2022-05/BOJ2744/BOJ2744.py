# 2744번 대소문자 바꾸기
# https://www.acmicpc.net/problem/2744
from curses.ascii import islower
import sys, os
sys.stdin = open('{}/BOJ2744.txt'.format(os.path.dirname(os.path.realpath(__file__))))
s=(sys.stdin.readline())
tmp=''
for c in s:
    if c.islower():
        tmp+=c.upper()
    else:
        tmp+=c.lower()
print(tmp)