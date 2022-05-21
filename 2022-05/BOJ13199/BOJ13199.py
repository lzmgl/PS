# 13199번 치킨 먹고 싶다
# https://www.acmicpc.net/problem/13199
import sys, os
sys.stdin = open('{}/BOJ13199.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
for _ in range(T):
    p, m, f, c = map(int, sys.stdin.readline().split())
    res = m//p
    coupon=c*res
    bonus1=coupon//f
    ans1=res+bonus1
    ans2=m//p
    if coupon>=f:
        ans2+=(coupon-f)//(f-c)+1
    print(ans2-ans1)