# 2675번 문자열 반복
# https://www.acmicpc.net/problem/2675
import sys, os
sys.stdin = open('{}/BOJ2675.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T = int(input())
while T>0:
    source = list(sys.stdin.readline().split())
    num = int(source[0])
    words = source[1]
    new_words=''
    for word in words:
        new_words+=word*num
    print(new_words)
    T-=1