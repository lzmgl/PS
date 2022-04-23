# 3058번 짝수를 찾아라
# https://www.acmicpc.net/problem/3058
import sys, os
sys.stdin = open('{}/BOJ3058.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for _ in range(N):
    sumN=0
    minN=1000001
    data=list(map(int, sys.stdin.readline().split()))
    for item in data:
        if item%2==0:
            sumN+=item
            minN=min(minN, item)
    print(sumN, minN)