# 18110번 solved.ac
# https://www.acmicpc.net/problem/18110
import sys, os
sys.stdin = open('{}/BOJ18110.txt'.format(os.path.dirname(os.path.realpath(__file__))))

def newRound(n):
    return int(n)+1 if n-int(n)>=0.5 else int(n)
N=int(sys.stdin.readline())
if N==0:
    print(0)
    exit()
data = [int(sys.stdin.readline().strip()) for i in range(N)]
data.sort()
cut=round(newRound(N*(0.15)))
print(round(newRound(sum(data[cut:N-cut])/(N-(2*cut)))))