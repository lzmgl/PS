# 2309번 일곱 난쟁이
# https://www.acmicpc.net/problem/2309
import sys, os
    
sys.stdin = open('{}/BOJ2309.txt'.format(os.path.dirname(os.path.realpath(__file__))))
data = [int(sys.stdin.readline().strip()) for i in range(9)]
data.sort()
sumN=sum(data)
for i in range(9):
    for j in range(i+1,9):
        if (sumN-data[i]-data[j])==100:
            data.remove(data[j])
            data.remove(data[i])
            print(*data, sep='\n')
            exit()