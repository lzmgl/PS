# 11050번 이항 계수 1
# https://www.acmicpc.net/problem/11050
import sys, os
    
sys.stdin = open('{}/BOJ11050.txt'.format(os.path.dirname(os.path.realpath(__file__))))
A, B=map(int, sys.stdin.readline().split())
def bino_coef(n, k):
    if k > n:
        return 0

    # 1.
    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    # 2.
    def choose(times, got):
        # 3.
        if times == n:
            return got == k
        # 4.
        if cache[times][got] != -1:
            return cache[times][got]

	# 5.
        cache[times][got] = choose(times+1, got) + choose(times+1, got+1)
        return cache[times][got]

    # 6.
    return choose(0, 0)
print(bino_coef(A,B))