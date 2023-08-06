# 5218번 알파벳 거리
# https://www.acmicpc.net/problem/5218
import sys, os

sys.stdin = open("{}/BOJ5218.txt".format(os.path.dirname(os.path.realpath(__file__))))
t = int(input())

for _ in range(t):
    word_a, word_b = input().split()
    ans = []
    for i in range(len(word_a)):
        c = ord(word_b[i]) - ord(word_a[i])
        if c < 0:
            c += 26
        ans.append(c)
    print("Distances:", *ans)
