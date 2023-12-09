# 13711번 LCS 4
# https://www.acmicpc.net/problem/13711
import sys, os

sys.stdin = open("{}/BOJ13711.txt".format(os.path.dirname(os.path.realpath(__file__))))

import bisect

n = sys.stdin.readline()
A = map(int, sys.stdin.readline().split())
dic = dict.fromkeys(A, 0)
queue = []
B = map(int, sys.stdin.readline().split())
for idx, item in enumerate(B):
    dic[item] = idx
for idx, item in dic.items():
    s = bisect.bisect_left(queue, item)
    if s != len(queue):
        queue[s] = item
    else:
        queue += [item]
print(len(queue))
