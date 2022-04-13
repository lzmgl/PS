# 2587번
# https://www.acmicpc.net/problem/2587
import sys
data=[]
for _ in range(5):
    data.append(int(sys.stdin.readline()))
data.sort()
print(sum(data)//len(data))
print(data[2])