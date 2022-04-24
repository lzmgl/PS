# 2822번 점수 계산
# https://www.acmicpc.net/problem/2822
import sys, os
sys.stdin = open('{}/BOJ2822.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2822번 점수 계산
# https://www.acmicpc.net/problem/2822
import sys
data=[]
for i in range(8):
    data.append([i, int(sys.stdin.readline())])
data.sort(key=lambda x:-x[1])
res=[]
sumN=[]
for i in range(5):
    res.append(data[i][0])
    sumN.append(data[i][1])
print(sum(sumN))
res.sort()
add_list = [res[i] + 1 for i in range(len(res))]
print(*add_list)