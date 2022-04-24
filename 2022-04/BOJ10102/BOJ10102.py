# 10102번 개표
# https://www.acmicpc.net/problem/10102
import sys, os
sys.stdin = open('{}/BOJ10102.txt'.format(os.path.dirname(os.path.realpath(__file__))))
v=int(input())
a=input().count('A')
print('Tie' if v/2==a else 'AB'[a<v/2])