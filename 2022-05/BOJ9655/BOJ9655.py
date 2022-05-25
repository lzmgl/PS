# 9655번 돌 게임
# https://www.acmicpc.net/problem/9655
import sys, os
sys.stdin = open('{}/BOJ9655.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
if N%2 == 0:
    print('CY')
else:
    print('SK')