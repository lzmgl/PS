# 9656번 돌 게임 2
# https://www.acmicpc.net/problem/9656
import sys, os
sys.stdin = open('{}/BOJ9656.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
if N%2 != 0:
    print('CY')
else:
    print('SK')