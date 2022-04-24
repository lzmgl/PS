# 10809번 알파벳 찾기
# https://www.acmicpc.net/problem/10809
import sys, os
sys.stdin = open('{}/BOJ10809.txt'.format(os.path.dirname(os.path.realpath(__file__))))
word=sys.stdin.readline().rstrip()
for i in range(97, 123):
    print(word.find(chr(i)), end=' ')