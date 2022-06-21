# 1212번 8진수 2진수
# https://www.acmicpc.net/problem/1212
import sys, os
sys.stdin = open('{}/BOJ1212.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=(sys.stdin.readline().strip())
print(bin(int(N, 8))[2:])