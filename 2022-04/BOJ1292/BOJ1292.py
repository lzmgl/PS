# 1292번 쉽게 푸는 문제
# https://www.acmicpc.net/problem/1292
import sys, os
sys.stdin = open('{}/BOJ1292.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 1292번 쉽게 푸는 문제
# https://www.acmicpc.net/problem/1292
import sys
A, B=map(int,sys.stdin.readline().split())
data=[0]
sumN=0
for i in range(1, 1000):
    for j in range(i):
        data.append(i)
    if len(data)>1000:
        break
for i in range(A, B+1):
    sumN+=data[i]
print(sumN)