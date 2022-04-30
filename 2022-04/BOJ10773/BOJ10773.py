# 10773번 제로
# https://www.acmicpc.net/problem/10773
import sys, os
sys.stdin = open('{}/BOJ10773.txt'.format(os.path.dirname(os.path.realpath(__file__))))
K=int(sys.stdin.readline())
stack=[]
for _ in range(K):
    s=int(sys.stdin.readline())
    if s!=0:
        stack.append(s)
    else:
        stack.pop()
print(sum(stack))