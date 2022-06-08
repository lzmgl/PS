# 2193번 이친수
# https://www.acmicpc.net/problem/2193
import sys, os
sys.stdin = open('{}/BOJ2193.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
dp=[0]*(N+1)
dp[1]=len([1])
dp[2]=len([10])
dp[3]=len([100, 101])
dp[4]=len([1000, 1010, 1001])
dp[5]=len([10000, 10100, 10101, 10010])
dp[6]=len([100000, 101000, 100100, 100010, 100001, 101010, 101001, 100101])