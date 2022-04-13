# 9498번 시험 성적
# https://www.acmicpc.net/problem/9498
import sys, os
    
sys.stdin = open('{}/BOJ9498.txt'.format(os.path.dirname(os.path.realpath(__file__))))

N=int(sys.stdin.readline())

if N>89:
    print('A')
elif N>79:
    print('B')
elif N>69:
    print('C')
elif N>59:
    print('D')
else:
    print('F')