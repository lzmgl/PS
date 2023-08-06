# 11655번 ROT13
# https://www.acmicpc.net/problem/11655
import sys, os

sys.stdin = open("{}/BOJ11655.txt".format(os.path.dirname(os.path.realpath(__file__))))
tmp = sys.stdin.readline()
ans = ""
for c in tmp:
    i = ord(c)
    if i > 96:
        ans += chr((i - 84) % 26 + 97)
    elif i > 64:
        ans += chr((i - 52) % 26 + 65)
    elif i == 32:
        ans += " "
    else:
        ans += c
print(ans)
