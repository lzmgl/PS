# 1037번 약수
# https://www.acmicpc.net/problem/1037
import sys
N=int(sys.stdin.readline())
res=1
data = list(map(int, sys.stdin.readline().split()))
minN=min(data)
maxN=max(data)
print(minN*maxN)