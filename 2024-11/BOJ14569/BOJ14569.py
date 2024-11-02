# 14569번 시간표 짜기
# https://www.acmicpc.net/problem/14569
import sys, os

sys.stdin = open("{}/BOJ14569.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())
k_data = []
for i in range(N):
    t_k, *t_k_data = sys.stdin.readline().split()
    sumC = 0
    for c in t_k_data:
        sumC += 2 ** (int(c))
    k_data.append(bin(sumC))
M = int(sys.stdin.readline())
for i in range(M):
    t_p, *t_p_data = sys.stdin.readline().split()
    sumC = 0
    res = 0
    for c in t_p_data:
        sumC += 2 ** (int(c))
    for time in k_data:
        if ((sumC) & int(time, 2)) == int(time, 2):
            res += 1
    print(res)
