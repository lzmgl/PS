# 1007번 벡터 매칭
# https://www.acmicpc.net/problem/1007
import sys, os, math, itertools
sys.stdin = open('{}/BOJ1007.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import sys
import math
import itertools

T = int(sys.stdin.readline())
results = []

for _ in range(T):
    N = int(sys.stdin.readline())
    coords = []
    
    # 모든 좌표들의 총합
    x_total = 0
    y_total = 0
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        x_total += x
        y_total += y
        coords.append([x, y])
    
    res = math.inf
    combinations = list(itertools.combinations(coords, int(N/2)))
    combinations_len_half = int(len(combinations) / 2)
    for sum_coord in combinations[:combinations_len_half]:
        sum_coord = list(sum_coord)

		# 더해야하는 좌표 총합
        x1_total = 0
        y1_total = 0
        for x1, y1 in sum_coord:
            x1_total += x1
            y1_total += y1
        
        # 빼야하는 좌표 총합(= 모든 좌표들의 총합 - 더해야하는 좌표 총합)
        x2_total = x_total - x1_total
        y2_total = y_total - y1_total
        
        res = min(res, math.sqrt((x1_total - x2_total) ** 2 + (y1_total - y2_total) ** 2))

    results.append(res)

for result in results:
    sys.stdout.write(str(result)+'\n')
# def dist(x1, x2, y1, y2):
#     return (x1-x2)**2+(y1-y2)**2

# mid=[0,0]
# T=int(sys.stdin.readline())
# for _ in range(T):
#     ans=math.inf
#     x,y=0,0
#     N=int(sys.stdin.readline())
#     data=[]
#     for _ in range(N):
#         x, y = map(int, sys.stdin.readline().split())
#         mid[0]+=x
#         mid[1]+=y
#         data.append([x,y])
#     combis = list(itertools.combinations(data, N//2))
#     len_combis_half=len(combis)//2

#     for item in combis[:len_combis_half]:
#         sum_ord=list(item)
#         total_x, total_y = 0,0
#         for x1, y1 in sum_ord:
#             total_x+=x1
#             total_y+=y1
#         total_x2=mid[0]-total_x
#         total_y2=mid[1]-total_y
#         ans=min(ans,dist(total_x, total_x2, total_y, total_y2))
#     # print(ans)
#     print('%0.9f'%(math.sqrt(ans)))
#     # print(math.sqrt(ans))