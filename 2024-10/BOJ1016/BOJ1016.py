# 1016번 제곱 ㄴㄴ 수
# https://www.acmicpc.net/problem/1016
import sys, os, math
sys.stdin = open('{}/BOJ1016.txt'.format(os.path.dirname(os.path.realpath(__file__))))
# N, M=map(int,sys.stdin.readline().split())
# data = [x**2 for x in range(2, int(M**0.5)+1)]
# num_set=set()
# for item in data:
#     n = N//item**2
#     while(n<M+1):
#         if n-N>=0:
#             num_set.add(n-N)
#         n+=item
# print(M-N-len(num_set)+1)


min, max = map(int,sys.stdin.readline().split())

# limit : max의 제곱근
# num_set : 소수 제곱으로 나누어 떨어지는 수
limit = int(max**0.5)
num_set = set()

for i in range(2, limit+1):
	# min ~ max 사이의 첫 소수제곱으로 나누어떨어지는 수 찾기
    roop = (min//i**2)*(i**2)
    if roop < min:
        roop += i**2
    
    # 제외 시키기
    for r in range(roop, max+1, i**2):
        num_set.add(r)

# 1도 포함이므로 +1
print(max-min-(len(num_set))+1)