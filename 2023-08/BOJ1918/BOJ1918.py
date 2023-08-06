# 1918번 후위 표기식
# https://www.acmicpc.net/problem/1918
import sys, os

sys.stdin = open("{}/BOJ1918.txt".format(os.path.dirname(os.path.realpath(__file__))))
data = sys.stdin.readline().strip()
depth2 = ["*", "/"]
depth3 = ["+", "-"]


def oper(data):
    str_ = data
    ans = ""
    stack = []
    for i in range(len(str_)):
        if str_[i] == "(":
            stack.append(str_[i])
        elif str_[i] in depth2:
            while stack and stack[-1] in depth2:
                ans += stack.pop()
            stack.append(str_[i])
            pass
        elif str_[i] in depth3:
            while stack and stack[-1] != "(":
                ans += stack.pop()
            stack.append(str_[i])
        elif str_[i] == ")":
            while stack and stack[-1] != "(":
                ans += stack.pop()
            stack.pop()
        else:
            ans += str_[i]
    while stack:
        ans += stack.pop()
    return ans


print(oper(data))
