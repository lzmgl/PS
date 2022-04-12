# 2908번 상수
# https://www.acmicpc.net/problem/2908
import sys
a, b=sys.stdin.readline().split()
a=a[::-1]
b=b[::-1]
print(max(int(a),int(b)))