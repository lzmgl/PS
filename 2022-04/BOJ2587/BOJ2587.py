# 2587번 대표값2
# https://www.acmicpc.net/problem/2587
import sys, os
sys.stdin = open('{}/BOJ2587.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2587번
# https://www.acmicpc.net/problem/2587
import sys
data=[]
for _ in range(5):
    data.append(int(sys.stdin.readline()))
data.sort()
print(sum(data)//len(data))
print(data[2])