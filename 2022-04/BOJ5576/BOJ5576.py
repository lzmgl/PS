# 5576번 콘테스트
# https://www.acmicpc.net/problem/5576
import sys, os
sys.stdin = open('{}/BOJ5576.txt'.format(os.path.dirname(os.path.realpath(__file__))))
w=[]
k=[]
for _ in range(10):
    w.append(int(sys.stdin.readline()))
for _ in range(10):
    k.append(int(sys.stdin.readline()))
w.sort()
k.sort()
score_w = w[7]+w[8]+w[9]
score_k = k[7]+k[8]+k[9]
print(score_w,score_k)