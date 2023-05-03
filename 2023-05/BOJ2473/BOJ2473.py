# 2473번 세 용액
# https://www.acmicpc.net/problem/2473
import sys, os
sys.stdin = open('{}/BOJ2473.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import math
def sol():
    target=0
    t1, t2, t3 = 0, 0, 0
    _min=math.inf
    for i in range(N-2): 
        start=i+1
        end=N-1
        while start < end:
            result = data[i]+data[start]+data[end]

            
            if abs(result) < abs(_min):
                t1, t2, t3 = data[i], data[start], data[end]
                _min = result

            if  result == target:
                t1, t2, t3 = data[i], data[start], data[end]
                print(t1, t2, t3)
                exit()
            elif result < target:
                start +=1
            else:
                end -=1

    print(t1,t2,t3)
if __name__ == '__main__':
    N=int(sys.stdin.readline())
    data=list(map(int, sys.stdin.readline().split()))
    data.sort()
    sol()




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