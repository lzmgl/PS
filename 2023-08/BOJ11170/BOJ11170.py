# 11170번 0의 개수
# https://www.acmicpc.net/problem/11170
import sys, os

sys.stdin = open("{}/BOJ11170.txt".format(os.path.dirname(os.path.realpath(__file__))))
t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    cnt = 0
    for i in range(n, m + 1):
        cnt += str(i).count("0")
    print(cnt)
