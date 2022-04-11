# 2576번
# https://www.acmicpc.net/problem/2576
import sys
sumN=0
minN=9999
for i in range(7):
    tmp=int(sys.stdin.readline())
    if tmp%2!=0:
        sumN+=tmp
        minN=min(minN,tmp)
if minN>100:
    print(-1)
    exit()
print(sumN)
print(minN)