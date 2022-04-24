# 5543번 상근날드
# https://www.acmicpc.net/problem/5543
import sys, os
sys.stdin = open('{}/BOJ5543.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 5543번 상근날드
# https://www.acmicpc.net/problem/5543
import sys
burger=[]
coke=[]
for _ in range(3):
    burger.append(int(sys.stdin.readline()))
for _ in range(2):
    coke.append(int(sys.stdin.readline()))
print(min(burger)+min(coke)-50)