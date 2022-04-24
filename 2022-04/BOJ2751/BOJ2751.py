# 2751번 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
import sys, os
sys.stdin = open('{}/BOJ2751.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2751번 수 정렬하기2
# https://www.acmicpc.net/problem/2751
import sys
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()
print(*data,sep='\n')