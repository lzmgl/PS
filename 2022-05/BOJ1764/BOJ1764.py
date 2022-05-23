# 1764번 듣보잡
# https://www.acmicpc.net/problem/1764
import sys, os
sys.stdin = open('{}/BOJ1764.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, M=map(int,sys.stdin.readline().split())
hear=set()
see=set()
for _ in range(N):
    hear.add(sys.stdin.readline().strip())
for _ in range(M):
    see.add(sys.stdin.readline().strip())
hear_see=hear&see
hear_see=list(hear_see)
hear_see.sort()
print(len(hear_see))
for item in hear_see:
    print(item)