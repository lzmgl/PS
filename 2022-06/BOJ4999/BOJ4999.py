# 4999번 아!
# https://www.acmicpc.net/problem/4999
import sys, os
sys.stdin = open('{}/BOJ4999.txt'.format(os.path.dirname(os.path.realpath(__file__))))
a=(sys.stdin.readline().strip())
b=(sys.stdin.readline().strip())
if len(a)>=len(b):
    print('go')
else:
    print('no')