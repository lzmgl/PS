# 소수
# https://www.acmicpc.net/problem/2581
import sys
minN=10001
sumN=0
M=int(sys.stdin.readline().rstrip())
N=int(sys.stdin.readline().rstrip())
for item in range(M,N+1):
    if item<2:
        continue
    isPrime=True
    for i in range(2, item):
        if item%i==0:
            isPrime=False
            break
    if isPrime:
        if minN>10000:
            minN=item
        sumN+=item
if sumN==0:
    print(-1)
    exit()
print(sumN)
print(minN)