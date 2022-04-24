# 10988번 팰린드롬인지 확인하기
# https://www.acmicpc.net/problem/10988
import sys, os
sys.stdin = open('{}/BOJ10988.txt'.format(os.path.dirname(os.path.realpath(__file__))))
word=input()
print(+(word[::-1]==word))