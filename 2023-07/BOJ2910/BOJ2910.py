# 2910번 빈도 정렬
# https://www.acmicpc.net/problem/2910
import sys, os
sys.stdin = open('{}/BOJ2910.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import Counter
N, C=map(int,sys.stdin.readline().split())
data=list(map(int, sys.stdin.readline().split()))
counter = Counter(data)
for item in counter.most_common():
    for _ in range(item[1]):
        print(item[0], end=' ')