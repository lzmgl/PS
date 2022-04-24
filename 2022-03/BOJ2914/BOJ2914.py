# 2914번 저작권
# https://www.acmicpc.net/problem/2914
import sys, os
sys.stdin = open('{}/BOJ2914.txt'.format(os.path.dirname(os.path.realpath(__file__))))
num, m = map(int, sys.stdin.readline().split())
print(num*(m-1)+1)