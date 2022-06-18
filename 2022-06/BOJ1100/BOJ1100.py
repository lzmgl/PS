# 1100번 하얀 칸
# https://www.acmicpc.net/problem/1100
import sys, os
sys.stdin = open('{}/BOJ1100.txt'.format(os.path.dirname(os.path.realpath(__file__))))
data=[sys.stdin.readline().strip() for _ in range(8)]
cnt=0
for i in range(8):
    for j in range(8):
        if i%2:
            if j%2:
                if data[i][j]=='F':
                    cnt+=1
        else:
            if not j%2:
                if data[i][j]=='F':
                    cnt+=1
print(cnt)