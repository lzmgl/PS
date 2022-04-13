# 10809번 알파벳 찾기
# https://www.acmicpc.net/problem/10809
import sys
word=sys.stdin.readline().rstrip()
for i in range(97, 123):
    print(word.find(chr(i)), end=' ')