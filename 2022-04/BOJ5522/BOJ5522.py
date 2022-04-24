# 5522번 카드 게임
# https://www.acmicpc.net/problem/5522
import sys, os
sys.stdin = open('{}/BOJ5522.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())import sys
tmp=0
for _ in range(5):
    tmp+=int(sys.stdin.readline())
print(tmp)