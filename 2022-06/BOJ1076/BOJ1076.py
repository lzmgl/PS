# 1076번 저항
# https://www.acmicpc.net/problem/1076
import sys, os
sys.stdin = open('{}/BOJ1076.txt'.format(os.path.dirname(os.path.realpath(__file__))))
data={'black':0 ,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}
tmp=''
for _ in range(2):
    tmp+=str(data[sys.stdin.readline().strip()])
print(int(tmp)*pow(10,data[sys.stdin.readline().strip()]))