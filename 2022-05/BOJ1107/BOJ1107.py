# 1107번 리모컨
# https://www.acmicpc.net/problem/1107
import sys, os
sys.stdin = open('{}/BOJ1107.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
err=list(map(int,sys.stdin.readline().split())) 