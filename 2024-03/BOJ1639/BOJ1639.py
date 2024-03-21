# 1639번 행운의 티켓
# https://www.acmicpc.net/problem/1639
import sys, os

sys.stdin = open("{}/BOJ1639.txt".format(os.path.dirname(os.path.realpath(__file__))))

S = sys.stdin.readline().strip()
num = len(S)
n = num // 2
S = int(S)
print(S)
print(n, num)
while n > 0:
    left = S // (10 ** (num - n))
    right = S % (10**n)
    if sum(map(int, str(left))) == sum(map(int, str(right))):
        break
    n -= 1
print(n)
