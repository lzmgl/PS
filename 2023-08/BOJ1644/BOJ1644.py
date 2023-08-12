# 1644번 소수의 연속합
# https://www.acmicpc.net/problem/1644
import sys, os
sys.stdin = open('{}/BOJ1644.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
import math
dp = [True for _ in range(4000001)]
dp[0] = dp[1] = False
che = [0]
for i in range(2, int(math.sqrt(N))+1): 
    if not dp[i]:
        continue 
    print(che)
    che.append(che[-1]+i)
    j=2
    while i*j < 4000001:
        dp[i*j]=False
        j+=1

l,r = 0,1
cnt=0
# print(che)
while r<len(che):
    sumN=che[r]-che[l]
    if sumN<N:
        r+=1
    elif sumN>N:
        l+=1
    else :
        cnt+=1
        r+=1
print(cnt)
print(che)