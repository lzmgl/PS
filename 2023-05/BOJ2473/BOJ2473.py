# 2473번 세 용액
# https://www.acmicpc.net/problem/2473
import sys, os
sys.stdin = open('{}/BOJ2473.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import math
N=int(sys.stdin.readline())
data=list(map(int, sys.stdin.readline().split()))
data.sort()
t1, t2, t3 = 0, 0, 0
_min=math.inf
target=0
for i in range(N):
    for j in range(i+1, N):
        
        start=j+1
        end=N-1
        while start <= end:
            mid = (start + end) // 2
            result = data[i]+data[j]+data[mid]

            if abs(result) <= abs(_min):
                t1, t2, t3 = data[i], data[j], data[mid]
                _min = result

            if  result == target:
                t1, t2, t3 = data[i], data[j], data[mid]
                print(t1, t2, t3)
                exit()
            elif result < target:
                start = mid + 1
            else:
                end = mid -1

print(t1,t2,t3)


# for i in range(N-2):
#     left, right = i+1, N-1
    
    
#     while left < right:
#         result = data[i]+data[left]+data[right]
        
#         if abs(result) <= abs(_min):
#             t1, t2, t3 = data[i], data[left], data[right]
#             _min = result
        
#         if result > 0:
#             right -= 1
#         elif result < 0:
#             left += 1
#         else:
#             print(t1, t2, t3)
#             exit()

# print(t1, t2, t3)