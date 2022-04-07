import sys
Hour, Minute, Second = map(int, sys.stdin.readline().split(':'))
Hour2, Minute2, Second2 = map(int, sys.stdin.readline().split(':'))
tmp1, tmp2, tmp3 = Hour2-Hour, Minute2-Minute, Second2-Second
if tmp3<0:
    tmp2-=1
    tmp3+=60
if tmp2<0:
    tmp1-=1
    tmp2+=60
if tmp1<0:
    tmp1+=24
print(f'{tmp1:02}:{tmp2:02}:{tmp3:02}')