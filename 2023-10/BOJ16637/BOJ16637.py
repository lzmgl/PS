# 16637번 괄호 추가하기
# https://www.acmicpc.net/problem/16637
import sys, os

sys.stdin = open("{}/BOJ16637.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())
data = sys.stdin.readline().strip()

num = []
op = []

for i, c in enumerate(data):
    if i % 2 == 0:  # 숫자
        num.append(int(c))
    else:  # 연산자
        op.append(c)

ans = -float("inf")


def oper(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b


def dfs(idx, val):
    global ans
    if idx == len(num) - 1:
        ans = max(ans, val)
        return
    dfs(idx + 1, oper(op[idx], val, num[idx + 1]))
    if idx + 2 <= len(num) - 1:
        tmp = oper(op[idx + 1], num[idx + 1], num[idx + 2])
        dfs(idx + 2, oper(op[idx], val, tmp))
    return


dfs(0, num[0])
print(ans)
