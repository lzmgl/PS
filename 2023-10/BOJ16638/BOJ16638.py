# 16638번 괄호 추가하기 2
# https://www.acmicpc.net/problem/16638
import sys, os

sys.stdin = open("{}/BOJ16638.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline()) // 2
eq = sys.stdin.readline()
result = -1e12
for bit in range(1 << N):
    if bit & (bit << 1):
        continue
    eq1 = [*eq]
    for i in reversed(range(N)):
        if bit & (1 << i):
            eq1.insert(i * 2 + 3, ")")
            eq1.insert(i * 2, "(")
    result = max(result, eval("".join(eq1)))
print(result)
