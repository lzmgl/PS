# 5176번 대회 자리
# https://www.acmicpc.net/problem/5176
import sys, os

sys.stdin = open("{}/BOJ5176.txt".format(os.path.dirname(os.path.realpath(__file__))))
t = int(sys.stdin.readline())
for _ in range(t):
    p, m = map(int, sys.stdin.readline().split())
    cnt = 0
    visit = [1] * (m + 1)
    for _ in range(p):
        num = int(sys.stdin.readline())
        if visit[num]:
            visit[num] -= 1
        else:
            cnt += 1
    print(cnt)
