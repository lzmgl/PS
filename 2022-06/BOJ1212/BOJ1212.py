# 1212번 8진수 2진수
# https://www.acmicpc.net/problem/1212
import sys, os
sys.stdin = open('{}/BOJ1212.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
cnt=sum=0
while N>0:
    tmp=N%10
    tmp*=pow(8, cnt)
    sum+=tmp
    cnt+=1
    N//=10
print(bin(sum)[2:])