# 10807번 개수 세기
# https://www.acmicpc.net/problem/10807
import sys
N=int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
v=int(sys.stdin.readline())
cnt=0
for item in data:
    if v==item:
        cnt+=1
print(cnt)