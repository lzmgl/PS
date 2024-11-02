# 2417번 정수 제곱근 부동소수점
# https://www.acmicpc.net/problem/2417
import sys, os
import math

sys.stdin = open("{}/BOJ2417.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())
if N != math.isqrt(N) ** 2:
    print(math.isqrt(N) + 1)
else:
    print(math.isqrt(N))
