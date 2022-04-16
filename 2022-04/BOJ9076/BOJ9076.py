# 9076번 점수 집계
# https://www.acmicpc.net/problem/9076
import sys, os
    
sys.stdin = open('{}/BOJ9076.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for _ in range(N):
    tmp=list(map(int, sys.stdin.readline().split()))
    tmp.remove(max(tmp))
    tmp.remove(min(tmp))
    maxN, minN = max(tmp), min(tmp)
    if maxN-minN>=4 :
        print("KIN")
    else:
        print(sum(tmp))