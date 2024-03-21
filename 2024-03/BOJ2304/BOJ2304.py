# 2304번 창고 다각형
# https://www.acmicpc.net/problem/2304
import sys, os

sys.stdin = open("{}/BOJ2304.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())
data = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))
data.sort()
high_idx = 0
highest = 0
for x, (_, y) in enumerate(data):
    if highest < y:
        high_idx = x
        highest = y
area = 0

left_data = data[:high_idx]
right_data = data[high_idx + 1 :]

# left area
x1, y1 = data[0]
for nx, ny in left_data:
    if ny < y1:
        pass
    else:
        area += (nx - x1) * y1
        x1 = nx
        y1 = ny
area += (data[high_idx][0] - x1) * y1
# right area
x1, y1 = data[-1]
for nx, ny in right_data[::-1]:
    if ny < y1:
        pass
    else:
        area += (x1 - nx) * y1
        x1 = nx
        y1 = ny

area += (x1 - data[high_idx][0]) * y1
area += highest
print(area)
