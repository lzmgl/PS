# 3460번 이진수
# https://www.acmicpc.net/problem/3460
import sys
idx=-1
T=int(sys.stdin.readline())
data=[]
for _ in range(T):
    n=int(sys.stdin.readline())
    binN=str(bin(n))[2:][::-1]
    while True:
        idx = ((binN.find('1', idx+1)))
        if idx==-1:
            break
        data.append(idx)
print(*data)