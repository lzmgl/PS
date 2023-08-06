# 11365번 !밀비 급일
# https://www.acmicpc.net/problem/11365
import sys, os

sys.stdin = open("{}/BOJ11365.txt".format(os.path.dirname(os.path.realpath(__file__))))
while 1:
    tmp = sys.stdin.readline().strip()
    if tmp == "END":
        break
    print(tmp[::-1])
