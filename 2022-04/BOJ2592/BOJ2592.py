# 2592번 대표값
# https://www.acmicpc.net/problem/2592
import sys, os
sys.stdin = open('{}/BOJ2592.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2592번 대표값
# https://www.acmicpc.net/problem/2592
import sys
meanN=modN=0
data=[]
idxs=[0]*1001
for _ in range(10):
    data.append(int(sys.stdin.readline()))
    idxs[data[_]]+=1
print(sum(data)//len(data))
print((idxs.index(max(idxs))))