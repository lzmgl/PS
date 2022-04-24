# 1259번 팰린드롬수
# https://www.acmicpc.net/problem/1259
import sys, os
sys.stdin = open('{}/BOJ1259.txt'.format(os.path.dirname(os.path.realpath(__file__))))
while N:=input():
    if N=='0':
        exit()
    if N==N[::-1]:
        print('yes')
    else:
        print('no')