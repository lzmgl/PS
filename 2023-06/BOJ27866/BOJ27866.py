# 27866번 문자와 문자열
# https://www.acmicpc.net/problem/27866
import sys, os
sys.stdin = open('{}/BOJ27866.txt'.format(os.path.dirname(os.path.realpath(__file__))))
S=sys.stdin.readline()
i=int(sys.stdin.readline())
print(S[i-1])