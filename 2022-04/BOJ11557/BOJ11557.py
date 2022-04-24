# 11557번 Yangjojang of The Year
# https://www.acmicpc.net/problem/11557
import sys, os
sys.stdin = open('{}/BOJ11557.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T = int(sys.stdin.readline())
for _ in range(T):
    maxNum=0
    res=''
    N = int(sys.stdin.readline())
    for _ in range(N):
        name, amount = sys.stdin.readline().split()
        if int(amount)>=maxNum:
            maxNum=int(amount)
            res=name
    print(res)