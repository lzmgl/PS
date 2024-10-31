# 31403번 $A + B - C$
# https://www.acmicpc.net/problem/31403
import sys, os

sys.stdin = open("{}/BOJ31403.txt".format(os.path.dirname(os.path.realpath(__file__))))
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

print(a + b - c)
print(int(str(a) + str(b)) - c)
