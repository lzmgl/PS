# 14928번 큰 수 (BIG)
# https://www.acmicpc.net/problem/14928
import sys, os

sys.stdin = open("{}/BOJ14928.txt".format(os.path.dirname(os.path.realpath(__file__))))
print(int(sys.stdin.readline()) % 20000303)
