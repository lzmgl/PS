# 8741번 이진수 합
# https://www.acmicpc.net/problem/8741
import sys, os
sys.stdin = open('{}/BOJ8741.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
'''
1)
1
2)
1 + (2+3)
10 11 = 6
3)
001 010 011 100 101 110 111 = 28
1 + (2+3) + (4+5+6+7)
4)
1 + 2+3 + 4+5+6+7+ 8+9+10+11+12+13+14+15 = 92 + 28 = 120
sum(2^N)
'''
# print(sum([x for x in range(2**int(sys.stdin.readline()))]))
# 시간초과
# 1~n-1까지 합 = n(n-1)//2
print(bin((2**N)*((2**N)-1)//2)[2:])