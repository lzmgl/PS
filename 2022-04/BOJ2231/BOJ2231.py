# 2231번 분해합
# https://www.acmicpc.net/problem/2231
import sys, os
sys.stdin = open('{}/BOJ2231.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for i in range(1, N):
    num=i
    word = str(num)
    sumN=0
    for c in word:
        sumN+=int(c)
    sumN+=num
    if sumN==N:
        print(num)
        exit()
print(0)