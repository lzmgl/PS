# 2162번 선분 그룹
# https://www.acmicpc.net/problem/2162
import sys, os

sys.stdin = open("{}/BOJ2162.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())

for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    print(data)
