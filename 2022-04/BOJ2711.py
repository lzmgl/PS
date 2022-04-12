# 2711번 오타맨 고창영
# https://www.acmicpc.net/problem/2711
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    missNum, word = sys.stdin.readline().split()
    missNum=int(missNum)
    word=word[:missNum-1]+word[missNum:]
    print(word)