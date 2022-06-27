# 11718번 그대로 출력하기
# https://www.acmicpc.net/problem/11718
import sys, os
sys.stdin = open('{}/BOJ11718.txt'.format(os.path.dirname(os.path.realpath(__file__))))
s=(sys.stdin.readlines())
for item in s:
    print(item.strip())