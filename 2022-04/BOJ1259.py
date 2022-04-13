# 1259번
# https://www.acmicpc.net/problem/1259
import sys
while N:=input():
    if N=='0':
        exit()
    if N==N[::-1]:
        print('yes')
    else:
        print('no')