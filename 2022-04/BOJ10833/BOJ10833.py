# 10833번 사과
# https://www.acmicpc.net/problem/10833
import sys, os
sys.stdin = open('{}/BOJ10833.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
appleSum=0
for _ in range(N):
    studentNum, apple = map(int, sys.stdin.readline().split())
    appleSum+=apple%studentNum
print(appleSum)