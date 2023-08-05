# 1918번 후위 표기식
# https://www.acmicpc.net/problem/1918
import sys, os

sys.stdin = open("{}/BOJ1918.txt".format(os.path.dirname(os.path.realpath(__file__))))
data = sys.stdin.readline()
depth2 = ["*", "/"]
depth3 = ["+", "-"]


def oper(data):
    str_ = data
    ans = ""
    stack = []
    boom = str_.count("(")
    for i in range(len(str_) - (2 * boom)):
        if str_[i] == "(":
            tmp = str_[::-1]
            idx = (len(str_) - 1) - tmp.find(")")

            str_ = str_[: i - 1] + oper(str_[i + 1 : idx]) + str_[idx + 1 :]
        elif str_[i] in depth2:
            stack.append(str_[i])
            pass
        elif str_[i] in depth3:
            pass
        else:
            ans += str_[i]
    if stack:
        for item in stack:
            ans += stack.pop()

    return ans


print(oper(data))
