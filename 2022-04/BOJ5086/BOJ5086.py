# 5086번 배수와 약수
# https://www.acmicpc.net/problem/5086
import sys, os
sys.stdin = open('{}/BOJ5086.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())while (s:=input())>'0 0':
    a,b=map(int,s.split(' '))
    if a%b==0:
        print("multiple")
    elif b%a==0:
        print("factor")
    else:
        print("neither")
'''
while a:a,b=map(int, input().split())