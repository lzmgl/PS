# 2108번 통계학
# Counter 최빈값 통계학
# https://www.acmicpc.net/problem/2108
import sys, os
sys.stdin = open('{}/BOJ2108.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import Counter
N=int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(N)]
data.sort()
print(round(sum(data)/N))
print(data[N//2])
cnts=(Counter(data).most_common())
if len(cnts) > 1:
    if cnts[0][1] == cnts[1][1]:
        print(cnts[1][0])
    else:
        print(cnts[0][0])
else:
        print(cnts[0][0])
print(data[N-1]-data[0])