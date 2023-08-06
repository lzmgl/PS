# 2902번 KMP는 왜 KMP일까?
# https://www.acmicpc.net/problem/2902
import sys, os

sys.stdin = open("{}/BOJ2902.txt".format(os.path.dirname(os.path.realpath(__file__))))
tmp = sys.stdin.readline().split("-")
ans = ""
for i in range(len(tmp)):
    ans += tmp[i][0]
print(ans)
