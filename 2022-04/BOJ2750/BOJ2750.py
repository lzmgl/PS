# 2750번 수 정렬하기
# https://www.acmicpc.net/problem/2750
import sys, os
sys.stdin = open('{}/BOJ2750.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2750번 수 정렬하기
# https://www.acmicpc.net/problem/2750
import sys
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()
print(*data,sep='\n')