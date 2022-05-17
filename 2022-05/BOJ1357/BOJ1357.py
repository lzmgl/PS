# 1357�� ������ ����
# https://www.acmicpc.net/problem/1357
import sys, os
sys.stdin = open('{}/BOJ1357.txt'.format(os.path.dirname(os.path.realpath(__file__))))
X, Y=map(int,sys.stdin.readline().split())

print(int(str(int(str(X)[::-1])+int(str(Y)[::-1]))[::-1]))