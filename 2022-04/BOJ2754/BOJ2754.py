# 2754번 학점계산
# https://www.acmicpc.net/problem/2754
import sys, os
sys.stdin = open('{}/BOJ2754.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())score = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
'F': 0.0}
print(score[input()])