# 18870번 좌표 압축
# https://www.acmicpc.net/problem/18870
import sys, os
sys.stdin = open('{}/BOJ18870.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
my_list2 = []
for i in range(N):
    my_list2.append([my_list[i], i])

my_list2.sort()
# -10 -9 2 4 4
index = 0
for i in range(0, len(my_list2)-1):
    my_list2[i].append(index)
    if my_list2[i][0] == my_list2[i+1][0]:
        continue
    else:
        index += 1

my_list2[-1].append(index)

for i in my_list2:
    i[0], i[1] = i[1], i[0]

my_list2.sort()
for item in my_list2:
    print(item[2])