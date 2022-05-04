# 2743번 단어 길이 재기
# https://www.acmicpc.net/problem/2743
import sys, os
sys.stdin = open('{}/BOJ2743.txt'.format(os.path.dirname(os.path.realpath(__file__))))
s=(sys.stdin.readline().rstrip())
print(len(s))