# 11654번 아스키 코드
# https://www.acmicpc.net/problem/11654
import sys, os
sys.stdin = open('{}/BOJ11654.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=(sys.stdin.readline().rstrip())
print(ord(N))
#print(ord(input()))