# 2711번 오타맨 고창영
# https://www.acmicpc.net/problem/2711
import sys, os
sys.stdin = open('{}/BOJ2711.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2711번 오타맨 고창영
# https://www.acmicpc.net/problem/2711
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    missNum, word = sys.stdin.readline().split()
    missNum=int(missNum)
    word=word[:missNum-1]+word[missNum:]
    print(word)