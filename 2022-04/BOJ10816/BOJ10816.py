# 10816번 숫자 카드 2
# https://www.acmicpc.net/problem/10816
import sys, os
    

sys.stdin = open('{}/BOJ10816.txt'.format(os.path.dirname(os.path.realpath(__file__))))

N=int(sys.stdin.readline())
dataN=list(map(int, sys.stdin.readline().split()))
dataN.sort()
M=int(sys.stdin.readline())
dataM=list(map(int, sys.stdin.readline().split()))
dicN={}
for i in dataN:
    if i not in dicN:
        dicN[i]=1
    else:
        dicN[i]+=1
for item in dataM:
    try:
        print(dicN[item])
    except:
        print(0)