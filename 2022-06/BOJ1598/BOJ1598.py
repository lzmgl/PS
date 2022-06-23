# 1598번 꼬리를 무는 숫자 나열
# https://www.acmicpc.net/problem/1598
import sys, os
sys.stdin = open('{}/BOJ1598.txt'.format(os.path.dirname(os.path.realpath(__file__))))
a, b=map(int,sys.stdin.readline().split())
at=((a-1)%4)
bt=((b-1)%4)
ap=((a-1)//4)
bp=((b-1)//4)
# if ap==bp:
#     print(abs(at-bt))
# if at>0:
#     ap+=1
# if bt>0:
#     bp+=1
# if at==bt:
#     print(abs(ap-bp))
#     exit()
print(abs(at-bt)+abs(ap-bp))