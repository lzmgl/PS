# 20529번 가장 가까운 세 사람의 심리적 거리
# https://www.acmicpc.net/problem/20529
import sys, os
sys.stdin = open('{}/BOJ20529.txt'.format(os.path.dirname(os.path.realpath(__file__))))

T=int(sys.stdin.readline())

def charCheck(str1, str2):
    sumN=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            sumN+=1
    return sumN
def sol(a, b, c):
    ans=charCheck(a,b)
    ans+=charCheck(c,b)
    ans+=charCheck(a,c)
    return ans

for _ in range(T):
    N=int(sys.stdin.readline().strip())
    minN=0
    data=sys.stdin.readline().strip().split()

    if N>32:
        print(minN)
    else:
        minN=9999

        for i in range(N-2):
            for j in range(N-1):
                for k in range(N):
                    if i == j or j == k or i == k:
                        continue
                    minN=min(sol(data[i], data[j], data[k]), minN)
        print(minN)
