# 10814번 나이순 정렬
# https://www.acmicpc.net/problem/10814
# list정렬
import sys
N=int(sys.stdin.readline())
data=[]
for i in range(N):
    age, Name = sys.stdin.readline().strip().split()
    age=int(age)
    data.append([i, age, Name])
data.sort()
data.sort(key=lambda x:x[1])
for i in range(N):
    print(*data[i][1:])
    