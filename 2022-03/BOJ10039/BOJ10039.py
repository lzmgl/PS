# 10039번 평균 점수
# https://www.acmicpc.net/problem/10039
import sys, os
sys.stdin = open('{}/BOJ10039.txt'.format(os.path.dirname(os.path.realpath(__file__))))
scores = []
for i in range(5):
    tmp = int(sys.stdin.readline())
    if tmp<40:
        tmp=40
    scores.append(tmp)
print(int(sum(scores)/len(scores)))