# 22966번 가장 쉬운 문제를 찾는 문제
# https://www.acmicpc.net/problem/22966
import sys, os

sys.stdin = open("{}/BOJ22966.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())
minN = 5
for i in range(N):
    tmp, s = sys.stdin.readline().split()
    if int(s) < minN:
        answer = tmp
        minN = int(s)
print(answer)
