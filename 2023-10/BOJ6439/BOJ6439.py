# 6439번 교차
# https:#www.acmicpc.net/problem/6439
import sys, os

sys.stdin = open("{}/BOJ6439.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())


def ccw(p1, p2, p3):
    ans = (
        p1[0] * p2[1]
        + p2[0] * p3[1]
        + p3[0] * p1[1]
        - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])
    )
    if ans > 0:
        return 1
    elif ans < 0:
        return -1
    return 0


# def det(p1, p2, p3, p4):
#     ccw1 = ccw(p1, p2, p3)
#     ccw2 = ccw(p1, p2, p4)
#     ccw3 = ccw(p3, p4, p1)
#     ccw4 = ccw(p3, p4, p2)

#     if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
#         if (
#             (min(p1[0], p2[0]) > max(p3[0], p3[0]))
#             or (min(p1[1], p2[1]) > max(p3[1], p4[1]))
#             or (min(p3[0], p3[0]) > max(p1[0], p2[0]))
#             or (min(p3[1], p4[1]) > max(p1[1], p2[1]))
#         ):
#             return False

#     if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
#         return True
#     return False


def isCross(a, b, c, d):
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    if ab == 0 and cd == 0:
        # 겹치는 부분이 있는지 확인
        # first 비교 후, second 비교
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return c <= b and a <= d

    else:
        return ab <= 0 and cd <= 0


def isInside(x, xl, xr, yt, yb):
    return xl < x[0] and x[0] < xr and yb < x[1] and x[1] < yt


def determine(data):
    x1, y1, x2, y2 = data[:4]  # line
    p1 = (x1, y1)
    p2 = (x2, y2)

    a, b, c, d = data[4:]  # rect
    xl = min(a, c)
    xr = max(a, c)
    yt = max(b, d)
    yb = min(b, d)

    r1 = (xl, yt)
    r2 = (xl, yb)
    r3 = (xr, yt)
    r4 = (xr, yb)

    print(p1, p2, r1, r2, r3, r4)
    if (
        det(r1, r2, p1, p2)
        and det(r1, r3, p1, p2)
        and det(r3, r4, p1, p2)
        and det(r2, r4, p1, p2)
    ):
        return "T"
    return "F"


for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    print(determine(data))
